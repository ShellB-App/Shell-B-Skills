---
name: audit-code
description: "Review or audit Shell:B's own code (or a Code workspace) and write findings that hold up: map it, read it, prove every claim with file:line. Use when asked to review, audit, scrutinize or find bugs or security problems in the code, or to recommend fixes and features from it."
author: Shell:B
authorUrl: https://github.com/ShellB-App/Shell-B
license: MIT
version: "1.0"
tags: [shell-b, code-review, audit, built-in]
---

# Audit code

A review is only worth what it can prove. The owner will check your findings against the code, so every one needs a
place in the code that shows it. A short review that is right beats a long one that is padded or guessed.

Stay read-only unless the owner asked for changes: for Shell:B itself use `shellb_self` actions `outline`, `source` and
`read_log`; they read the live code and need no workspace.

## 1. Map before you read
- `outline` with no path, then on `server` and `ui/src`: every file with its size and purpose.
- Pick the files that matter for the request (security → auth.py, the fetchers, file serving, sandbox, self-mod;
  a feature → its module and its UI). Say which ones you chose and why.
- `outline` each chosen file to see its functions, routes and line ranges.

## 2. Read what you judge
- Read the code behind each finding with `source path=… offset=<first line> limit=<span>` (`paths` reads up to 8
  files in one call). Every partial read tells you the range you got and where to continue; follow it rather than
  reading from line 1 again.
- If the same lines come back twice, stop and change the arguments. Don't keep calling.

## 3. Prove it, or drop it
- **Something is wrong:** quote the line and give `file:line`. Explain the concrete failure: an input, a request or a
  sequence that goes wrong.
- **Something is missing** ("no X", "doesn't do Y"): search for it first with `source query=<regex>` (try two or three
  names). Most "missing" features already exist under another name. If the search finds nothing, say what you searched.
- **A recommendation:** check the code doesn't already do it (sandbox flags, iframe `sandbox=`, indexes, limits).
- Rate severity by what an attacker or a bug can actually do on this box (one owner, localhost trust, LAN + Tailscale),
  not by how it sounds.
- **Earlier reports** (in this chat, a past chat or an artifact) are not evidence. Re-check every finding you carry
  over against the code and drop it if the code says otherwise.
- Leave out generic advice that fits any project (import order, magic numbers, "add a CHANGELOG") unless you can tie
  it to a real problem here.

## 4. Report honestly
- Your last tool call before writing the report must be `read_log`. Copy its first line ("This turn read N files:
  …") into **Scope** word for word, and list the important files you did not read. Never claim more than it lists:
  reading the first 60 lines of a file is not auditing it.
- Shape: **Scope** (what you read) · **Findings** most severe first, each with `file:line`, evidence, impact and fix ·
  **Checked and fine** (things you verified are already right) · **Not covered**.
- Mark each finding *confirmed* (you read the code and traced it) or *suspected* (needs a closer look).
