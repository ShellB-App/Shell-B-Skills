---
name: shellb-screensaver
description: Build a Shell:B screensaver (a full-window Canvas 2D animation in a Studio Screensaver project) when the user asks for a screensaver, idle screen or ambient animation for Shell:B; covers the rules it must follow to run for hours, the project files, previewing, and packaging it for the Shell-B-Screensavers community repository.
author: Shell:B
authorUrl: https://github.com/ShellB-App/Shell-B
license: MIT
version: "1.0"
tags: [shell-b, screensaver, canvas, animation, studio]
---

# Building a Shell:B screensaver

A Shell:B screensaver is a Studio project of kind **Screensaver**: one `index.html` that animates forever with
nobody touching it. When the owner picks it (Settings → Appearance → Screensaver style, or the *Use as screensaver*
button on the project), Shell:B shows `index.html` full screen in a sandboxed iframe whenever the computer is idle,
and any key or mouse movement dismisses it. The frame allows scripts only: no same-origin access, no network, no
audio.

Use this skill when the user asks for a screensaver, an idle screen, or an ambient animation "for Shell:B". A
screensaver for another product is a Motion project, not this.

## 1. Where the work happens

Screensavers are built inside a Screensaver project, where you have `project_save_file` and `project_read_file`.

- **In a Screensaver project already**: write `index.html` (replace the skeleton) and keep `DESIGN.md` honest (the
  brief, the palette, the tuning constants).
- **In a plain chat**: you cannot create projects from here. Ask the user to start one: Settings → Appearance →
  *Make one in the Studio*, or Studio → New project → Screensaver, then describe the piece there. Offer to design it
  now in words (concept, palette, motion) so the project brief is ready.

## 2. Decide the piece before coding

One idea, stated in a sentence, that reads well at 3 a.m. with nobody watching: a koi pond from above, ink in slow
water, a harmonograph drawing roses, a starfield, weather on a window, cellular automata, drifting geometry. Then
decide what changes over minutes (seasons, palette drift, new formations) so it never feels looped, and what the
first frame looks like, because previews and covers capture the first second.

## 3. The rules (Shell:B's own, from the Studio guide)

- Fill any aspect ratio: handle `resize`, no letterboxing, 4:3 to ultrawide and portrait.
- Canvas 2D first; SVG or CSS are fine. No WebGL (the preview browser has none).
- A `requestAnimationFrame` loop with `dt` clamped (≤ 0.05 s), `devicePixelRatio` capped at 2, a pause while
  `document.hidden`. No growth over hours: fixed-size particle pools, typed arrays, never append DOM nodes in the loop.
- Calm on the GPU; dark by default (it runs at night); nothing static and bright (OLED): drift every element slowly.
- No controls, chrome, hover states or cursor (`cursor: none`). No audio, no network, no external URLs: everything
  in the project folder.
- `prefers-reduced-motion`: slow to a gentle drift (multiply speeds by 0.25–0.3), never stop.
- Shell:B may draw its clock over the lower-left (about 30 % wide, 25 % tall): keep that corner calm.
- Tuning constants (counts, speeds, palette) together at the top of the script.
- Pre-roll: run `draw()` for a second or two of simulated time before the first real frame so the first frame is
  already a composition, not an empty canvas.
- Canvas colours with alpha: write `hsl(h s% l% / a)`; the older `hsla(h s% l% a)` form is invalid and draws black.

Start from `template/index.html` in this skill (the Studio's own skeleton: sized canvas, clamped loop, resize,
reduced motion). `references/koi-pond-notes.md` shows how a finished piece is organised.

## 4. Check it

- Preview with the project's **Preview** button (full screen, as the screensaver will show it); watch the first
  frame and the lower-left corner.
- Resize the window; rotate to portrait if you can.
- Leave it running for an hour in a tab and watch memory in the task manager: flat, not climbing.
- Reduced motion on: still moving, slowly.

Then *Use as screensaver* on the project header, and tell the user where to change the idle delay (Settings →
Appearance → Screensaver).

## 5. Sharing it with the community

Screensavers live in github.com/ShellB-App/Shell-B-Screensavers. A folder `screensavers/<id>/` holds:

```
saver.json     {"name", "blurb", "author", "authorUrl", "license", "version", "tags", "clockSafe", "credits"}
index.html     the piece, relative paths only
preview.jpg    a frame from the first seconds, about 640×360, under 400 KB
assets/        optional
```

`clockSafe: true` means the lower-left stays calm. `credits` names any font, texture or borrowed code with its
license (it must allow redistribution). `python3 -I scripts/validate.py` in the repo enforces the rules above
(external URLs, fetch, sockets and audio are rejected), builds `index.json` and the README gallery;
`scripts/preview.sh screensavers/<id>` makes the preview with headless Firefox. People who don't use git can open a
*Submit a screensaver* issue with a link to the files. The author's name and link appear in every Shell:B that
installs it, so never submit someone else's work as your own.
