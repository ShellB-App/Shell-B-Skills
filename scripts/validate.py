#!/usr/bin/env python3
"""Check every skill in skills/<name>/ and build index.json and the listing in README.md.

A skill is a folder with a SKILL.md (YAML front matter: name, description, plus author/license here) and optional
scripts, templates and references. The format is Claude's Agent Skills, which Shell:B's Community Hub reads directly:
it lists every folder holding a SKILL.md and installs one with a click. Standard library only; run from the root:

    python3 -I scripts/validate.py          # check + rebuild index.json and the README listing
    python3 -I scripts/validate.py --check  # check only (CI); exits 1 on any error or stale generated file
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
README = ROOT / "README.md"
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")
URL_RE = re.compile(r"^https?://[^\s\"'<>]{1,200}$")
START, END = "<!-- skills:start -->", "<!-- skills:end -->"
ALLOWED = {".md", ".txt", ".json", ".yaml", ".yml", ".py", ".sh", ".js", ".ts", ".html", ".css", ".svg", ".png", ".jpg", ".jpeg", ".webp", ".csv", ".toml"}
MAX_FILE, MAX_FOLDER, MAX_FILES = 2 * 2**20, 10 * 2**20, 200
SECRETS = (re.compile(r"\b(ghp|gho|github_pat)_[A-Za-z0-9_]{20,}"), re.compile(r"\bsk-[A-Za-z0-9]{20,}"), re.compile(r"AKIA[0-9A-Z]{16}"),
           re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"))


def front_matter(md: str) -> tuple[dict, str]:
    """A tolerant reader for the YAML front matter (plain key: value lines, quoted or not; a >- / | block for description)."""
    m = re.match(r"^﻿?---\s*\n(.*?)\n---\s*\n?(.*)$", md, re.S)
    if not m:
        return {}, md
    meta, key = {}, None
    for line in m.group(1).splitlines():
        if line.startswith((" ", "\t")) and key:
            meta[key] = (meta[key] + " " + line.strip()).strip()
            continue
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        key = k.strip()
        v = v.strip()
        meta[key] = "" if v in (">", ">-", "|", "|-") else v.strip("\"'")
    return meta, m.group(2)


def check(folder: Path) -> tuple[dict | None, list[str], list[str]]:
    errors, warnings = [], []
    name = folder.name
    if not NAME_RE.match(name):
        errors.append(f"folder name {name!r}: lowercase letters, digits and dashes only")
    md = folder / "SKILL.md"
    if not md.is_file():
        return None, ["no SKILL.md"], []
    text = md.read_text(errors="replace")
    meta, body = front_matter(text)
    if not meta:
        return None, ["SKILL.md has no front matter (--- name / description ---)"], []
    if meta.get("name") != name:
        errors.append(f"front matter name {meta.get('name')!r} must equal the folder name {name!r}")
    desc = str(meta.get("description") or "").strip()
    if not desc:
        errors.append("description is required: what the skill does and when an agent should use it")
    elif len(desc) > 600:
        warnings.append("description is over 600 characters; Shell:B truncates it in the catalogue")
    elif len(desc) < 40:
        warnings.append("description is short; say when to use the skill, not only what it is")
    for key in ("author", "license"):
        if not meta.get(key):
            errors.append(f"{key} is required in the front matter (license: an SPDX id such as MIT or CC0-1.0)")
    if meta.get("authorUrl") and not URL_RE.match(meta["authorUrl"]):
        errors.append("authorUrl must be an http(s) URL")
    words = len(body.split())
    if words < 80:
        warnings.append(f"the body is {words} words; a skill is a playbook, not a note")
    if words > 6000:
        warnings.append(f"the body is {words} words; agents load it whole, so keep the core short and move detail to references/")
    total, count = 0, 0
    for p in folder.rglob("*"):
        if p.is_symlink():
            errors.append(f"{p.relative_to(folder)}: symbolic links aren't allowed")
            continue
        if not p.is_file():
            continue
        rel = p.relative_to(folder)
        count += 1
        if any(part.startswith(".") for part in rel.parts):
            errors.append(f"{rel}: hidden files aren't allowed")
        if p.suffix.lower() not in ALLOWED and p.name not in ("LICENSE", "LICENSE.txt", "Makefile"):
            errors.append(f"{rel}: file type {p.suffix or '(none)'} isn't allowed")
        size = p.stat().st_size
        if size > MAX_FILE:
            errors.append(f"{rel} is over {MAX_FILE // 2**20} MB")
        total += size
        if p.suffix.lower() in (".md", ".txt", ".json", ".yaml", ".yml", ".py", ".sh", ".js", ".ts", ".html", ".css", ".toml"):
            content = p.read_text(errors="replace")
            for rx in SECRETS:
                if rx.search(content):
                    errors.append(f"{rel}: looks like it contains a credential")
                    break
    if total > MAX_FOLDER or count > MAX_FILES:
        errors.append(f"the folder is over {MAX_FOLDER // 2**20} MB or {MAX_FILES} files")
    return {"meta": meta, "words": words, "files": count}, errors, warnings


def listing_html(index: list[dict]) -> str:
    rows = []
    for it in index:
        by = html.escape(it["author"])
        if it.get("authorUrl"):
            by = f'<a href="{html.escape(it["authorUrl"], quote=True)}">{by}</a>'
        rows.append(f'<tr><td><a href="{it["path"]}"><b>{html.escape(it["name"])}</b></a></td><td>{html.escape(it["description"])}</td>'
                    f'<td><sub>{by} · {html.escape(it["license"])}</sub></td></tr>')
    return f"{START}\n<table>\n<tr><th>Skill</th><th>What it does</th><th>Credit</th></tr>\n" + "\n".join(rows) + f"\n</table>\n{END}"


def readme_with_listing(index: list[dict]) -> str | None:
    text = README.read_text()
    if START not in text or END not in text:
        return None
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    return head + listing_html(index) + tail


def main() -> int:
    check_only = "--check" in sys.argv
    index, bad, stale = [], 0, []
    for folder in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        res, errors, warnings = check(folder)
        for w in warnings:
            print(f"  {folder.name}: warning: {w}")
        for e in errors:
            print(f"  {folder.name}: ERROR: {e}")
        if errors or res is None:
            bad += 1
            continue
        m = res["meta"]
        index.append({"name": folder.name, "description": str(m.get("description") or "").strip(), "author": m.get("author", ""),
                      "authorUrl": m.get("authorUrl", ""), "license": m.get("license", ""), "version": m.get("version", "1.0"),
                      "tags": [t.strip() for t in str(m.get("tags") or "").strip("[]").split(",") if t.strip()],
                      "path": f"skills/{folder.name}/SKILL.md", "words": res["words"], "files": res["files"]})
    idx = json.dumps({"format": 1, "kind": "skill", "items": index}, indent=1, ensure_ascii=False) + "\n"
    readme = readme_with_listing(index)
    if check_only:
        if not (ROOT / "index.json").exists() or (ROOT / "index.json").read_text() != idx:
            stale.append("index.json")
        if readme is not None and readme != README.read_text():
            stale.append("README.md (listing)")
        for s in stale:
            print(f"  stale: {s} (run scripts/validate.py and commit)")
    else:
        (ROOT / "index.json").write_text(idx)
        if readme is not None:
            README.write_text(readme)
    print(f"{len(index)} skill{'s' if len(index) != 1 else ''} ok, {bad} with errors" + (f", {len(stale)} generated file(s) stale" if stale else ""))
    return 1 if bad or stale else 0


if __name__ == "__main__":
    sys.exit(main())
