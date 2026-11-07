---
name: stage-8
description: Course notes for stage 8 of the chatbot course (02_web/stage8/app.py and 02_web/stage8/index.html): what the stage adds, the predict question, the expected behaviour and the common fixes. Load when the learner asks about stage 8 or about 02_web/stage8/app.py and 02_web/stage8/index.html.
metadata:
  opencode/autoinvoke: "true"
---
# Stage 8: 02_web/stage8/app.py and 02_web/stage8/index.html

## What this stage adds

One route GET / sends the page. The page keeps the list in a JavaScript array named history, sends all of it to /chat on every turn, and appends the reply. Nothing else changes; test_chat.py still passes. Five optional modifications to app.py, each with a prediction and a test, are in 02_web/stage8/modifications.md; explain their lines, do not write them.

## Two lines a learner often asks about

- `await fetch("/chat", {...})` in index.html sends the request from the page and waits for the response. `body: JSON.stringify({ history })` turns the array into the JSON text the route reads with `request.get_json()`.
- `Path(__file__).with_name("index.html").read_text()` under label 3a reads the page file that sits next to app.py and returns its text, which is why the page has no address of its own.

## The predict question

After you refresh the page, what does the chatbot remember?

## What the learner should see

Open http://localhost:8000, type the three memory turns, and the memory test passes. Refresh the page and type turn 2 again: the model cannot name Sunday, because the array was created empty again when the page loaded. The browser's developer tools (macOS: Command, Option and I; Windows: F12; then the Network tab) shows the request named chat and its body, which is the whole list.

## Common messages and what they mean

- 'Method Not Allowed' means the address /chat was typed into the browser; go back to the page address.
- '"GET /favicon.ico HTTP/1.1" 404' in the server log means the browser asked for a tab icon and there is none. 404 is the status number for not found; the page works without an icon.
- A log line the learner did not cause, such as '"GET /health HTTP/1.1" 404' every thirty seconds, comes from a tool on the laptop (an editor or a browser tool that watches local servers) asking whether a server is alive. It is not a fault, and its absence means nothing on that laptop is polling. It is the learning moment of the log: the server answers every caller and cannot tell the page from any other caller, which is why stage 9 adds the passphrase and modification 3 checks the length before paying for a call.
- If the page looks unchanged after an edit, refresh it.
- The page does not load: the server is not running, or the address is not localhost:8000.
