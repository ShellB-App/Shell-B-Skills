---
name: summarize-documents
description: "Summarize documents, meeting recordings, long email threads or web pages into what the reader needs: the gist, the decisions, the numbers and who has to do what by when. Use when the user asks to summarize, sum up, recap, condense or get the key points or action items from a file, a recording, a meeting, an email thread or a link."
author: Shell:B
authorUrl: https://github.com/ShellB-App/Shell-B
license: MIT
version: "1.0"
tags: [summary, documents, meetings, work, action-items]
---

# Summarizing documents and meetings

A summary saves someone from reading the whole thing, so it has to be faithful: nothing invented, nothing important
left out, and the reader can find the source of every point. Write in the user's language, even when the document is
in another one.

## 1. Get the whole source

| Source | How to read it |
|---|---|
| PDF, Word, Excel, PowerPoint, OpenDocument, EPUB | `read_document`; then `view_document` for charts, tables or slides whose meaning is in the picture |
| Scan, photo of a page, screenshot | `ocr` (engine `vision` for tables, forms and handwriting) |
| Audio or video (a meeting, a call, a talk) | `transcribe` with the file or link |
| An email or thread | `read_email` action `search`, then `read` for each message |
| A web page | `web_fetch` (follow `start` to read past the first part) |
| Something from an earlier chat or project | `library` or `recall_conversations` |

Read all of it. If a tool returns only part (a long document or transcript is clipped), keep reading until the end,
or say clearly which part your summary covers. Never summarize from the title or the first page alone.

## 2. Pick the shape

Ask yourself what the reader will do with it, and choose. Don't ask the user unless it really isn't clear.

- **Gist** (default): three to five sentences, then up to eight bullet points of the key facts.
- **Meeting notes:** date and who was there (if known) · decisions made · action items as a table (*who*, *what*,
  *by when*) · open questions · anything that needs a follow-up meeting.
- **Report or contract:** purpose · main findings or obligations · numbers and dates · risks, conditions, deadlines,
  anything unusual or that the reader might not expect.
- **Email thread:** where it stands now · what each person wants · what is asked of the user, and by when.
- **Comparison of several documents:** a short table of how they differ on the points that matter, then a line on
  what that means.

If the user asked for a length ("one paragraph", "for my boss in two lines"), keep to it.

## 3. Be faithful

- Every number, name, date and amount must come from the source. Copy them exactly; keep units and currencies.
- Mark what is the document's claim versus a fact you checked. Your own opinion, if asked for, goes in a separate
  section, labelled as yours.
- Point to where things are: page or slide numbers for documents, timestamps for recordings (`transcribe` gives
  them), the sender and date for emails.
- If something is ambiguous or contradicts itself, say so rather than picking one reading.
- Keep confidential material where it is: don't paste it into web searches.

## 4. Deliver

- Short summaries go straight in the reply. Longer ones (meeting notes, a report digest) go in `create_artifact`
  (Markdown) so they can be copied, exported and updated.
- In a chat Project, offer to keep it with `project_save_file` (for example `YYYY-MM-DD-team-meeting.md`).
- Offer the obvious next step in one line, if there is one: draft the follow-up email (the `email-drafting` skill),
  add the deadlines as reminders with `schedule_task`, or translate the summary with `translate`.
