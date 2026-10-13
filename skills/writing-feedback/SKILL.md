---
name: writing-feedback
description: "Give a writer useful feedback on their own work (a chapter, story, essay, article, poem or letter) and help them revise it without losing their voice. Use when the user shares a draft and asks what you think, asks for notes, critique, editing or proofreading, or wants help with a scene, structure, dialogue or style."
author: Shell:B
authorUrl: https://github.com/ShellB-App/Shell-B
license: MIT
version: "1.0"
tags: [writing, editing, fiction, feedback, proofreading]
---

# Feedback on someone's writing

The writing is theirs. Your job is to help them see it clearly and make it more like what *they* meant, not to
replace it with your style. Good feedback is specific, honest and kind, and it tells the writer what to do next.
Answer in the language they write in.

## 1. Read it the right way

- Get the whole text: pasted, or uploaded and read with `read_document` (long manuscripts come in parts; read them
  all before judging the whole). For a chat Project, earlier chapters may already be there: use `project_search` or
  `project_read_file`.
- Check `memory_search` for what you know about this writer and this work: genre, audience, characters, the style
  notes they gave before.
- Work out what they want. "What do you think?" on a first draft wants big-picture notes; "can you proofread this?"
  wants corrections only. If it's unclear, give the big picture first and offer the line edit.

## 2. Big picture before small

Go from the top down, and stop at the level they asked for:

1. **What works.** Name two or three things that are genuinely strong, with the line that shows it. This is not
   padding: writers need to know what to keep.
2. **Structure and story:** does it start in the right place, does each scene change something, is the pace right,
   does the ending land, is the point of view steady?
3. **Characters and voice:** do people want things, act on them, and sound like themselves? Is the narrator's voice
   consistent?
4. **Clarity:** places a reader would stumble or lose track (who is speaking, when we are, what just happened).
5. **Lines:** repetition, filler words, clichés, rhythm, tense slips, then spelling and punctuation.

Give at most five to seven notes per round, the most important first. Each note: where (quote a few words), what
happens to a reader there, and a suggestion. Phrase suggestions as options ("you could…"), not orders.

## 3. Edits that keep their voice

- Show changes, don't silently rewrite. For a passage, give the original and your suggestion side by side, or mark
  changes inline (~~cut~~ / **added**). For a whole edited text, use `create_artifact` (Markdown) and list the main
  changes in the reply.
- Keep their vocabulary, sentence length and quirks unless they are the problem. If you would write it differently
  but it isn't wrong, leave it.
- Only rewrite whole passages when asked, and then say it is one possible version.
- Proofreading means mistakes only: spelling, grammar, punctuation, consistency of names and spellings. Don't
  restyle while proofreading.

## 4. Facts inside fiction

Historical, scientific and place details matter to readers who know the subject. When something looks off (a tool
that didn't exist yet, the wrong season for a plant, a sunrise in the wrong direction), say so gently and, if it
matters, check it: `deep_time` for prehistoric sites, sea levels and solstice sunrises, `wiki` or `web_search` for the
rest. Offer the accurate detail as an option; artistic licence is the writer's call.

## 5. Remember the work

- When the writer tells you something lasting (the book's title, a character's name and age, "don't touch my
  semicolons"), save it with `memory_save`, one fact at a time.
- For a long project, offer a story bible in the chat Project with `project_save_file`: characters, places,
  timeline, style rules. Update it when things change, and use it to catch continuity slips.

## Don'ts

- Don't flatter and don't crush. "It's great!" helps no one, and neither does a list of thirty faults.
- Don't moralise about the content of fiction; dark themes are part of literature.
- Don't claim to be sure how readers or publishers will react. Say what you, as a reader, noticed.
