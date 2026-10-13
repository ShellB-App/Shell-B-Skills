---
name: verify-chat
description: "Audit this chat when something may have gone wrong: a failed or stopped turn, a tool error, a wrong or made-up answer, a claim that a file was saved or a search was run when it wasn't. Use when the user says /verify-chat or asks you to check, verify, review or debug the conversation."
author: Shell:B
authorUrl: https://github.com/ShellB-App/Shell-B
license: MIT
version: "1.0"
tags: [shell-b, verify, debugging, built-in]
---

# Verify a chat

You are auditing a conversation that other Shell:B agents (often small local models) had with the user. Be the careful
second pair of eyes: find what is wrong, prove it from the record, and say how to fix it.

## 1. Get the record
Call `chat_transcript` first. It lists every message, numbered `#1`, `#2` and so on. For each reply it shows the agent,
the model, the turn status, and every tool call with its arguments, status and result. If the user pointed at a reply
("check reply #7"), focus there but still read what led to it. Call `chat_transcript` with `message=<n>` to see a
message's tool results in full when an excerpt is not enough.

## 2. Check it
Work through these, most important first:
- **Failures:** turns with status `error` or `stopped`, tool calls with status `error`, errors in tool results (a
  traceback, a non-zero exit code, "not found", a timeout). Name the cause if the record shows it.
- **Claims against evidence:** every "I searched / saved / ran / generated / verified" must match a tool call that
  succeeded. Every fact taken from a tool must match that tool's result. Flag anything invented, misread or
  overstated, and quote the record.
- **Correctness:** check the maths, code, logic, units, dates and facts yourself. Re-run code with `run_code` or
  re-check a fact with `web_search` / `web_fetch` when you have those tools and it matters.
- **Coverage:** parts of the user's request that were skipped, misunderstood or quietly dropped.
- **Loops and waste:** the same tool call repeated with no progress, or an agent stuck or going in circles.

Don't nitpick style. When everything checks out, say so plainly: a clean bill of health is a valid result.

## 3. Report
Use this shape:

**Verdict:** ✅ Looks right / ⚠️ Problems found / ❌ Broken. Then one sentence on why.

**Findings:** ordered by severity. Give each one the message number, what is wrong, and the evidence (quote the tool
result or the claim).

**Fix:** what to do next. Give the corrected answer when you can produce it yourself. If an agent should retry,
write the prompt to send. If the problem is in Shell:B itself (a broken tool, a bad setting, a model that can't
handle tool calls), say which one and what to change. Don't claim you fixed anything you didn't.
