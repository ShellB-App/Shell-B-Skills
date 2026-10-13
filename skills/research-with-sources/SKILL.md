---
name: research-with-sources
description: "Research a question properly and answer with sources the user can check: search, read the sources themselves, separate what is established from what is debated, and cite every claim. Use when the user asks to research, look into, dig up or fact-check a topic, wants sources or references, or asks about history, archaeology, science or anything where being right matters more than being quick."
author: Shell:B
authorUrl: https://github.com/ShellB-App/Shell-B
license: MIT
version: "1.0"
tags: [research, sources, citations, history, science, fact-check]
---

# Research with sources

A researched answer is only as good as the sources behind it. Read them, cite them, and be clear about how sure
anyone can be. A short answer the user can check beats a long one they have to take on trust.

## 1. Frame the question

- Restate the question in one line. If it is broad ("tell me about the Neolithic"), pick the angle that fits what you
  know of the user (`memory_search` for their interests) and say which angle you took; don't stop to ask unless the
  request could mean two very different things.
- For more than a quick fact, open a board with `research_board` action `start` (title, question). The user can
  browse every source and finding there, and it stays with the chat.

## 2. Gather sources

Use what fits, in roughly this order:

- **Specialist tools first** when the topic has one: `deep_time` for prehistoric sites, past sea levels and solstice
  alignments; `marine` for species names (WoRMS) and where they have been recorded (OBIS); `solar_system_ephemeris`
  or `local_sky_view` for the sky. These compute or look up real data; cite them by name.
- **`wiki`** for an offline encyclopedia overview (Wikipedia, Wikisource, Gutenberg for old texts). Good for orienting
  and for references to follow, not as the final word on a contested point.
- **`web_search`** with several phrasings, then **`web_fetch`** to read the pages. Prefer, in order: peer-reviewed
  papers and their abstracts, university and museum pages, excavation or agency reports, then reputable journalism.
  Treat forums, AI-written pages and sites selling something as leads, not sources.
- **The user's own files**: `read_document` for anything they uploaded, and `research_board` action `search` once
  sources are on the board.

Add each source you actually read to the board (`add`), with the quote or figure you took from it. Aim for at least
two independent sources for anything important, and say when you could only find one.

## 3. Weigh what you found

- Sort claims into **established** (sources agree), **debated** (serious sources disagree; give each side and who
  holds it) and **unknown** (nobody knows yet). Don't flatten a real debate into one answer.
- Check dates, numbers and names against a second source. Watch for units and dating conventions: BC/BCE vs. BP
  ("before present", counted from 1950), calibrated vs. uncalibrated radiocarbon dates, metric vs. imperial.
- Note how old a finding is. A 1970s interpretation may have been overturned; look for newer work.
- Popular claims ("the builders aligned it to the stars", "this species is extinct") need the strongest evidence.

## 4. Answer

- Lead with the direct answer in two or three sentences, then the detail.
- Cite as you go: [S1], [S2] when the board is open (use `research_board` action `synthesize` to write the cited
  summary there too), otherwise a link after the sentence it supports.
- End with what is still uncertain and, if useful, where to read more (one or two of the best sources).
- Never cite a page you didn't open, and never invent a reference, author, quote or page number. If you couldn't
  find something, say so; that is a useful answer.

## 5. Keep it

If the user is working on something over time (a book, a talk, a project), offer to keep the findings: the board
stays with the chat, `project_save_file` adds a summary to a chat Project, and `memory_save` remembers the interest
itself ("User is researching Neolithic passage tombs in Brittany for a novel.").
