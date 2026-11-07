---
name: stage-2
description: Course notes for stage 2 of the chatbot course (01_base/stage2.py): what the stage adds, the predict question, the expected behaviour and the common fixes. Load when the learner asks about stage 2 or about 01_base/stage2.py.
metadata:
  opencode/autoinvoke: "true"
---
# Stage 2: 01_base/stage2.py

## What this stage adds

A system entry at the top of the list (who the assistant is, the café facts, two rules) and three fixed questions sent in their own calls.

## Two lines a learner often asks about

- The system entry's `"content"` is several quoted pieces inside parentheses. Python joins them into one string; they are split across lines only so that the code is easier to read.
- `messages = [system_entry, {"role": "user", "content": question}]` builds a new two-entry list for each question, so the system entry is first in every call and no question sees another.

## The predict question

What will the reply to question 2, 'What is the capital of France?', do?

## What the learner should see

Question 1 is answered from the facts (open at 8 on Sundays). Question 2 gets the refusal sentence 'I can only help with questions about the café.' Question 3 is answered in at most two sentences. A broken rule is possible and is recorded as a cross; a rule is an instruction that the model usually follows and sometimes breaks.

## Common messages and what they mean

- A rule broken by the model is not a bug in the script; the test records it.
- Three questions are three calls; running the script twice quickly can reach the per-minute limit.
