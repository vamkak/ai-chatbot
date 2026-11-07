---
name: stage-1
description: Course notes for stage 1 of the chatbot course (01_base/stage1.py): what the stage adds, the predict question, the expected behaviour and the common fixes. Load when the learner asks about stage 1 or about 01_base/stage1.py.
metadata:
  opencode/autoinvoke: "true"
---
# Stage 1: 01_base/stage1.py

## What this stage adds

One call to the model with a list holding one user entry; the reply is printed.

## Two lines a learner often asks about

- The client is created once, under label 1, from two values read from .env; the call under label 3 uses it. Creating the client sends nothing; the call does.
- `{"role": "user", "content": "..."}` is one entry: `"role"` says who is speaking, and `"content"` is the text. The list holds one such entry, and the model receives only what is in the list.

## The predict question

Run the script twice. Will the second reply be exactly the same as the first?

## What the learner should see

Two runs give two different café names. With the # removed from the temperature line (temperature=0), the two runs are usually similar and sometimes identical, and never guaranteed identical. The script pauses once at the predict gate; the learner presses Enter.

## Common messages and what they mean

- 'The provider refused the request' with 401 or 'API key' means the key is wrong. With 429 or 'rate limit' it means too many requests in the last minute, or the day's allowance is used; the script's own last line says to wait one minute.
- If nothing happens after the run command, the script is waiting at the predict gate for Enter.
