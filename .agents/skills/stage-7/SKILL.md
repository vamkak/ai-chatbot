---
name: stage-7
description: Course notes for stage 7 of the chatbot course (02_web/stage7/app.py and test_chat.py): what the stage adds, the predict question, the expected behaviour and the common fixes. Load when the learner asks about stage 7 or about 02_web/stage7/app.py and test_chat.py.
metadata:
  opencode/autoinvoke: "true"
---
# Stage 7: 02_web/stage7/app.py and test_chat.py

## What this stage adds

Since stage 1 your program has been the caller of an API. From stage 7 your program is the one that is called. The loop, the typed input and the appends are removed. A Flask route (one address the server answers), POST /chat, receives the whole history as JSON (text in a fixed format that browsers and servers both read). It adds the system entry, trims, calls the model and returns one reply with the tokens number. The server keeps nothing. test_chat.py is the caller that keeps the list and sends the four fixed turns.

## The Flask lines a learner asks about

- Flask is a Python package that turns a function into an address a browser or a program can call. Four lines in app.py do that work; the rest of the file is stage 5.
- `from flask import Flask, request` (line 11) loads the package; request holds what the caller sent.
- `app = Flask(__name__)` (label 3) creates the server object.
- `@app.post("/chat")` (label 4) is the line above the function; it tells Flask to run the function below it when a POST request arrives at the address /chat. Without it the function is never called.
- `app.run(port=8000, debug=True)` (label 8) starts the server on the laptop; Vercel ignores it and starts the application its own way.
- `request.get_json()["history"]` reads the body of the request as JSON and takes the value under the key history, which is the caller's list.
- GET asks for a page; POST sends data. The route function is the body of the stage 5 loop without the typed input and the appends.
- If a learner asks about applications that store data, or about CRUD: they use the same route mechanism with one route for each action and a database behind the routes. This chatbot stores nothing, so it has one route, and storage is outside the course.

## The predict question

The test client sends the memory turns through the route. Will the memory test pass? What will the server's terminal show?

## What the learner should see

Terminal 1 (python 02_web/stage7/app.py) prints 'Running on http://127.0.0.1:8000' and then one line per request. Terminal 2 (python test_chat.py) prints the four turns and replies with tokens numbers; the memory test passes because the client resends the list. Stop the server with Ctrl+C, which the server itself names.

## Common messages and what they mean

- 'WARNING: This is a development server' is printed on every start, and nothing is wrong when it appears. It says that Flask's own server is for one developer on one laptop; Vercel starts the application its own way.
- `"GET / HTTP/1.1" 404` in the server's terminal means the learner opened the printed address in a browser. Stage 7 has one route, POST /chat, and no page; every browser address gets 404 until stage 8 adds GET /. The caller in stage 7 is test_chat.py in a second terminal, so nothing is wrong and nothing needs fixing.
- 'Restarting with stat' and 'Debugger PIN' are Flask's debug mode, switched on by debug=True in app.run: the server restarts when the file is saved. Nothing is wrong.
- 'Address already in use' means a server from earlier is still running; stop it with Ctrl+C in its terminal.
- 'Connection refused' from the test client means the server is not running or the address is not port 8000.
- 'No module named flask' or 'requests' means the virtual environment is not on in that terminal; run source .venv/bin/activate there, then the command again.
- A WSL terminal whose prompt shows a Windows path is on the wrong side; open a new terminal from the window opened in WSL.
