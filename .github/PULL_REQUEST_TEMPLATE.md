## What this adds

<!-- one or two sentences: what the skill teaches an agent to do, and when it should trigger -->

## Checklist

- [ ] `skills/<name>/SKILL.md` with front matter `name` (= folder), `description` (what + when), `author`, `license` (SPDX id)
- [ ] The description says *when* to use the skill; the body is a playbook with steps, not a note
- [ ] Anything bundled (scripts, templates, references) is referenced from SKILL.md and is mine or credited
- [ ] No credentials, no network calls to private services, nothing that assumes a tool Shell:B doesn't have
- [ ] `python3 -I scripts/validate.py` runs clean; `index.json` and the README listing are committed as generated
