---
name: shellb-theme-design
description: Design a custom Shell:B interface theme with the design_theme tool when the user asks for a new look, colours, mood or style for Shell:B itself (not for a website or project), then refine it from feedback and, if they want to share it, package it for the Shell-B-Themes community repository.
author: Shell:B
authorUrl: https://github.com/EveAeternam/Shell-B
license: MIT
version: "1.0"
tags: [shell-b, theme, design, appearance]
---

# Designing a Shell:B theme

A Shell:B theme is data, never CSS: a palette, two fonts from a fixed list, a corner shape, a backdrop (sky gradient,
soft glows, stars, a horizon silhouette) and a particle layer drifting behind the app. You make one by calling the
`design_theme` tool with the whole specification. Shell:B validates it (hex colours, fixed lists, text nudged to WCAG
contrast) and replies with a ```theme``` card the user can apply with one click. Revisions keep the same id.

Use this skill when the user wants Shell:B's own interface to look different: "make it feel like a rainy Tokyo
street", "a warmer light theme", "something like my favourite game's UI". Do not use it for a website, deck or
Studio project; those are built with files, not with `design_theme`.

## 1. Pick a direction before touching colours

Work like an art director. From the request, decide in one sentence what the theme *is*: a place, a time of day, a
material, a film. Everything after serves that sentence. Ask one question only if the request gives you nothing to
go on (mood, reference, light or dark); otherwise choose and explain afterwards.

Decide the mode: a theme designs **one** mode. Night scenes, consoles and cinemas are dark; paper, mornings, water
and snow are usually light. Dark themes use deep *tinted* neutrals (navy, plum, forest, charcoal with a hue), never
`#000000`. Light themes use warm or cool off-whites, never `#ffffff` as the page.

## 2. Build the palette (60 / 30 / 10)

| Key | Role | Rule |
|---|---|---|
| `bg` | page | the dominant 60 %: the tinted neutral |
| `panel` | sidebar, cards | one step toward the text colour; in dark themes slightly lighter than `bg`, in light themes slightly whiter |
| `raised`, `hover`, `code` | inputs/chips, selected rows, code | optional: Shell:B derives them from `panel` and `bg` if you leave them out |
| `text` | body text | needs 7:1 on `bg` and `panel` (Shell:B nudges it if not, but choose it yourself) |
| `text2`, `muted` | secondary text, labels | 4.5:1 on both surfaces |
| `accent` | buttons, links, focus | the 10 %: one strong colour, used sparingly; its label (white or near-black) must reach 4.5:1 |
| `brand` | logo, secondary highlights | a second colour that agrees with the accent, not a rival |
| `line` | borders | white for dark themes, near-black for light; drawn translucent |
| `inks` | picker stripe, button gradient | 2–4 signature colours in the order you want them seen |

Good accents are mid-saturation and clearly readable: brass on navy, vermilion on cream, teal on slate, lime on
forest. Avoid pale pastels as accents (they fail the label check) and avoid two loud accents.

## 3. Type, shape, backdrop, particles

- **Fonts**: `display` for headings from `inter`, `barlow`, `barlow-condensed` (technical), `shippori-mincho`
  (elegant serif), `josefin-sans` (airy geometric), `jetbrains-mono` (terminal), `georgia`, `cormorant-garamond`
  (cinematic), `sora` (cool, clean), `syncopate` (very wide caps), `outfit` (light modern), `zen-maru-gothic`
  (rounded, storybook). `body` only from the readable ones: `inter`, `barlow`, `shippori-mincho`, `georgia`,
  `sora`, `outfit`, `zen-maru-gothic`. `caps: true` with `tracking` 0.08–0.16 for console and sci-fi looks.
- **Shape**: `hard` (2 px radii, chamfered buttons: consoles, industrial), `soft` (default), `round` (pills and big
  radii: friendly, organic, water).
- **Backdrop**: `sky` 1–3 colours top to bottom; up to 4 `glows` (`x`, `y` in %, `size` 10–100, `strength`
  0.02–0.5): a moon, a sunset, lamplight, a nebula; `stars` 0–1 only for night skies; `horizon` from `none`,
  `forest`, `mountains`, `floating` (islands), `waves`, `city`, `seafloor`, `dunes`, `snowpines`, `hills`, with
  `horizonColor` darker than `bg` (or lighter, on light themes, for mist).
- **Particles**: `fireflies`, `petals`, `leaves`, `woodsprites`, `snow`, `embers`, `bubbles`, `bokeh`, `sand`,
  `rain` (wet window over city lights), `abyss` (jellyfish, marine snow), `aurora` (curtains plus snow), or `none`.
  `colors` 1–3, `density` 0.2–2 (1 is normal; 0.6–0.8 for calm themes). Particles must belong to the scene: no
  snow on a desert, no fireflies in a console.

## 4. Call the tool, then present it

Call `design_theme` once with everything: `name` (1–2 words), `blurb` (one sentence for the picker), `mode`,
`palette`, `inks`, `fonts`, `caps`, `tracking`, `shape`, `backdrop`, `particles`. Show the ```theme``` card the
tool gives you, then say in two sentences what the direction is and what to look at. If the tool reports
adjustments ("text #… → #… for contrast"), mention them only if they changed the look.

Refine from feedback with `revise_id` and the **whole** theme again, changing only what was asked. Typical asks and
the right knob: "too dark" → lift `bg` and `panel` a step, not `text`; "more alive" → particles or a glow, not more
accent; "hard to read" → raise `text2`/`muted` contrast, drop `caps`; "feels generic" → a horizon, a display font
with character, one bolder ink.

See `references/example-theme.json` for a complete, validated specification.

## 5. Sharing it with the community

Themes live in the Shell-B-Themes repository (github.com/EveAeternam/Shell-B-Themes), and anyone can add one. When
the user wants to share theirs:

1. Tell them to open Settings → Appearance, hover their theme under *Designed by Shell:B* and press the **Export**
   (download) button. That saves `<name>.theme.json` with their name prefilled as `author`.
2. The repository wants `themes/<id>/theme.json` (id: lowercase letters, digits, dashes), with `author`, optional
   `authorUrl`, `license` (an SPDX id: MIT, CC0-1.0, CC-BY-4.0), `version`, `tags`, and `credits` for anything not
   theirs. `python3 -I scripts/validate.py` in the repo checks it, draws `preview.svg`, updates `index.json` and the
   README gallery; CI refuses pull requests with errors or stale generated files.
3. Without git, they can open a *Submit a theme* issue in the repository and paste the JSON; a maintainer adds it
   with them as the author.

Credit matters: the author's name and link show in every Shell:B that installs the theme, in the README gallery and
in `index.json`. Never submit a theme in someone else's name, and don't copy a company's branding.
