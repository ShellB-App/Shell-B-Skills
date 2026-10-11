# Contributing a skill

1. Fork the repository and add `skills/<name>/SKILL.md` (name: lowercase letters, digits and dashes; it must be new).
   Put long reference material under `references/`, helper scripts under `scripts/`, starting files under `template/`.
2. Fill in the front matter: `name` (= the folder), `description` (what it does *and when to use it*), `author`,
   optional `authorUrl`, `license` (an SPDX id: MIT, CC0-1.0, CC-BY-4.0, Apache-2.0), `version`, `tags`. By opening a
   pull request you agree the skill is shared under the license you named. If you ported it from somewhere, say so and
   credit the original author.
3. Run `python3 -I scripts/validate.py` from the repository root and fix every error; read the warnings.
4. Try it in Shell:B: install the folder from Tools & Connectors → Skills (upload) or point the Community Hub at your
   fork, enable it, and ask an agent for the thing it teaches. Fix what the agent got wrong.
5. Commit the folder, `index.json` and `README.md` (the script rewrites its table), and open a pull request; the
   template has the checklist. Without git, open a *Submit a skill* issue and paste the SKILL.md.

Reviews check that the description triggers in the right situations, that the steps work with Shell:B's tools, and
that nothing in it needs credentials or reaches private services. Updating a skill: bump `version`, keep the name.
