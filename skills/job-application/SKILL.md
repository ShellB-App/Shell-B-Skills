---
name: job-application
description: "Help with a job hunt: find openings that fit, tailor a CV and cover letter to one posting, keep track of applications and prepare for interviews. Use when the user asks for help finding a job, applying for a position, writing or updating a CV, résumé or cover letter, or getting ready for an interview."
author: Shell:B
authorUrl: https://github.com/ShellB-App/Shell-B
license: MIT
version: "1.0"
tags: [jobs, career, cv, cover-letter, interview, writing]
---

# Job applications

Looking for work is tiring and personal. Be a practical helper: do the legwork, keep everything honest, and keep the
person in charge of what goes out under their name. Work in the user's language, and write each application in the
language of the posting.

## 1. Know the person first

- Check `memory_search` for "CV", "job", "career" and the field they mentioned. If you already know their background,
  say what you remember in one line and carry on.
- Otherwise ask for their CV (an upload is best; read it with `read_document`). If they have none, ask for the basics
  in one message: studies, past jobs and internships, skills, languages, where they can work, when they can start.
- Save what lasts with `memory_save`, one fact per call ("User is looking for marine biology jobs on the Atlantic
  coast, from September."). Never save their address, phone number or ID numbers.

## 2. Find openings

- Search with `web_search`, several times with different words: the job title and its synonyms, the field, the
  place, the contract type, in each language the user works in. Specialist fields have their own boards
  (universities, research institutes, NGOs, public agencies, professional societies): look for those, not only the
  big job sites.
- Read each promising posting with `web_fetch`. Keep only real, current postings: note the deadline and skip any
  that have closed.
- List them briefly: title, employer, place, deadline, link, and one line on why it fits or what is missing. Put
  the best fits first. Never invent a posting or a deadline; if a page won't load, say so.

## 3. Tailor the application to one posting

1. Pull out what the posting asks for: must-haves, nice-to-haves, the words it uses.
2. Match each one to something real in the CV. Say plainly where there is a gap; don't paper over it.
3. **CV:** reorder and reword so the matching experience comes first, using the posting's own words where they are
   true. Keep it to one or two pages. Never add a skill, degree, job or date the person doesn't have.
4. **Cover letter:** under one page. Open with the role and why this employer, then two or three short paragraphs
   that each prove one requirement with a concrete example, then a plain closing. No clichés ("I am a passionate team
   player"); show it instead. Ask the user for a real example when the CV doesn't give one.
5. Deliver each document with `create_artifact` (Markdown) so they can read, copy and export it. Mark anything you
   want them to check or fill in as **[to check]**.

## 4. Keep track

When there is more than one application, keep a tracker the user can open again:

- in a chat Project, with `project_save_file` (for example `applications.md`), or
- otherwise as a Markdown artifact with a table: employer, role, link, deadline, date sent, status, next step.

Update it whenever the user says they applied, heard back or have an interview. If they want a reminder before a
deadline or to follow up, offer to set one with `schedule_task`, written as a complete instruction.

## 5. Prepare for an interview

- Research the employer with `web_search` / `web_fetch`: what they do, recent news, the team if it's public.
- Write the eight to ten questions they are most likely to ask for this role, each with a short answer outline built
  from the person's real experience (situation, what they did, the result).
- Add three good questions for the person to ask them.
- Offer a practice round: ask one question at a time, wait for the answer, then give brief, kind, specific feedback.

## Rules

- Nothing is sent for them. If they ask you to email an application, draft it, and use `send_email` only when they
  ask for it to be sent (they approve every email).
- Be honest about fit. "This one asks for a diving certificate you don't have yet" helps more than false hope.
- Keep it encouraging and short. A job hunt is a long road; end with the next concrete step.
