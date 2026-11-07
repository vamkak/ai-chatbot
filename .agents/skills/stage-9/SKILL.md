---
name: stage-9
description: Course notes for stage 9 of the chatbot course (app.py, index.html and test_chat.py at the root): what the stage adds, the predict question, the expected behaviour and the common fixes. Load when the learner asks about stage 9 or about app.py, index.html and test_chat.py at the root.
metadata:
  opencode/autoinvoke: "true"
---
# Stage 9: app.py, index.html and test_chat.py at the root

## What this stage adds

A passphrase check. The page asks the visitor for a passphrase once and sends it with every request. The route answers 'The passphrase is wrong.' with status 401 when it does not match APP_PASSWORD. These are the files Vercel runs; the four values are set in Vercel's project settings.

## The predict question

Once the app is on Vercel, where is the key? What would happen if it were written in index.html?

## What the learner should see

The key is in Vercel's environment settings and in the root .env on the laptop, and it is not written in app.py, index.html or any file pushed to GitHub. A wrong passphrase gets the message with 401 without calling the model. git status must not list .env before the push. After the import, the link works after the passphrase is entered; the first request after a pause is slower because Vercel starts the program again after a pause.

## Common messages and what they mean

- If the build fails, requirements.txt is missing or its name is misspelled.
- Every reply is 'APP_PASSWORD is not set on this server.': that value is missing in Vercel's settings; add it under Settings, Environment Variables, then Redeploy.
- Every reply starts 'The provider refused the request': one of the three LLM values is wrong in Vercel's settings; check the names and values against .env, then Redeploy.
- The page says 'This page is unavailable' with FUNCTION_INVOCATION_FAILED: one of the three LLM values is missing, so the program stopped at the client line; add it, then Redeploy.
- Every reply is 'The passphrase is wrong.': the value on Vercel, the word typed on the page, and PASSPHRASE in test_chat.py are not all the same.
- The test client says Connection refused with localhost in the message: either the ADDRESS line in test_chat.py still holds the localhost address, or, when the learner is still testing on the laptop, the server in terminal 1 is not running.
