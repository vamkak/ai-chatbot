---
name: error
description: Read an error message, a traceback or a failed run with the learner, explain it in plain English, point to the line, and ask what they will change. Use whenever the learner pastes an error or says a script stopped.
metadata:
  opencode/slash: "true"
---
# Read an error with the learner

1. Ask the learner to paste the last ten lines the script printed, if they have not.
2. Find the error type and the message. Reply in bullets: one for what that type of error
   means, one for what the message says.
3. One bullet points to the line: the file, the line number from the traceback, and the
   line itself in backticks. If the script printed one of the course's own messages, explain
   that message and the action it names. The course's own messages are: "the virtual
   environment is not on"; "too old. The course needs Python 3.10 or newer"; "this is the
   Windows side"; "You are running Windows Python"; "Package missing"; "LLM_API_KEY is not
   set yet"; "The provider refused the key"; "The provider refused the request"; "I can
   only help with questions about the café."; "tokens sent: unknown"; "APP_PASSWORD is not
   set on this server"; and "The passphrase is wrong."
4. One bullet says in words what change would fix it, for example "move the line that
   creates history above the while line" or "run source .venv/bin/activate in this
   terminal, then the command again". A last bullet asks whether that matches what they
   see; if the learner proposes a different change, say whether it would work.

Four things a learner pastes are results and not faults, and say so: "I can only help with
questions about the café." as the reply to a question that is not about the café is rule 2
working, including the reply to "what was my last question?"; "WARNING: This is a
development server" is printed on every start of stage 7 onwards and nothing is wrong;
`"GET /health HTTP/1.1" 404` repeated every thirty seconds is a tool on the laptop asking
whether a server is alive, not the learner and not a fault; `"GET /favicon.ico HTTP/1.1" 404` in the server log is the browser asking for a tab icon
that does not exist; `"GET / HTTP/1.1" 404` in stage 7 is the browser opening the printed
address, which has no page until stage 8 adds GET /, so the learner runs test_chat.py in a
second terminal instead; and "Method Not Allowed" is the address `/chat` typed into the
browser, which sends a GET to a route that answers POST. Two messages come from Python
rather than the script: "can't open file" means the command was typed in the wrong
folder, so the learner goes to the repository root, the folder that holds check.py; and
"No module named" means the virtual environment is off in that terminal. A third comes from
the requests package: "Connection refused" at the end of a long traceback from test_chat.py,
with localhost and port 8000 in the message, means no server is running; the learner starts
app.py (or 02_web/stage7/app.py) in a second terminal with (.venv) in the prompt, leaves it
running, and runs test_chat.py again. The same message after stage 9 with localhost in it
means ADDRESS in test_chat.py was not changed to the Vercel link.

Do not type the corrected line; the learner types it. Never ask for or display the
contents of `.env` or a key.
