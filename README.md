# Build an AI chatbot in Python

This course builds a chatbot in stages, from one call to a language model to a deployed web application.

> **Licence:** [PolyForm Noncommercial 1.0.0](LICENSE). You may use this repository freely for your own learning and for non-commercial teaching; you may not use it as the curriculum of a fee-charging course. [NOTICE.md](NOTICE.md) explains in plain English what is allowed.
Every command below is typed at this folder, the root of the repository. There is one `.env`
file, here at the root; `check.py` creates it on the first run, and every stage finds it.

## Before the session

The earlier modules of the programme installed most of the tools for this course. Do the
steps below in order. The steps take approximately twenty minutes.

### Step 1: the terminal (Windows only)

1. Open the Ubuntu terminal: the app named **Ubuntu** in the Start menu, or the **Ubuntu**
   tab in Windows Terminal. This terminal is WSL (Windows Subsystem for Linux). Do not use
   PowerShell or Command Prompt for this course.
2. Type `pwd`. The terminal must print `/home/` followed by your user name. If it prints
   a path that starts with `/mnt/c/` or `C:\`, you are on the Windows side: close that
   terminal and open the Ubuntu terminal.
3. Do all the work of this course inside WSL. Do not use a path that starts with `/mnt/c/`.
   That path is the Windows side, and `check.py` stops there.

### Step 2: Python and git

1. Type `python3 --version`. The version must be 3.10 or newer. `check.py` stops an older
   Python.
2. Type `git --version`. The command must print a version.
3. If your prompt shows `(base)`, that is conda from an earlier module. Do not remove it.
   The course makes its own `.venv` on top of it.

### Step 3: accounts and keys

1. Make sure that you have a GitHub account. Make sure that your browser is signed in to it.
2. Make sure that you have a Vercel account. Sign in to Vercel with the same GitHub account.
3. Get a Gemini key from Google AI Studio. Get an OpenRouter key. Save both keys in a place
   where you can copy them.
4. Do not paste a key into `.env` before the session. The session tells you when to paste
   the Gemini key. Stage 6 tells you when to paste the OpenRouter key.

### Step 4: your own copy of this repository

Do not download the ZIP file. Do not clone the course repository itself. Stage 9 pushes your
work to GitHub, and Vercel builds from your account. Thus the repository must be yours.

1. Open https://github.com/SwarupSG/ai-chatbot-cohort in the browser that is signed in to
   GitHub.
2. Click **Use this template**, then **Create a new repository**.
3. Name the repository `ai-chatbot`. Keep it Private. Click **Create repository**.
4. On the page of your new repository, click **Code**. Copy the address under **HTTPS**.
5. In the terminal for the course (the Ubuntu terminal on Windows), type `cd ~`. Then type
   `pwd`. The terminal must print your home folder: `/home/<you>` in WSL, `/Users/<you>`
   on macOS. On Windows, a path that starts with `/mnt/c/` is the wrong place: go back to
   Step 1.
6. Type `git clone`, a space, and the address that you copied. Then type `cd ai-chatbot`.
7. Windows: type `code .` in the same terminal. VS Code opens this folder, and the
   bottom-left corner of the window shows "WSL: Ubuntu". macOS: open VS Code, then open
   the folder `ai-chatbot` with **File**, **Open Folder**.
8. From now on, type each command of this course in the terminal inside VS Code: **View**,
   **Terminal**. On Windows that terminal is already inside WSL.

### Step 5: git identity and sign-in

1. Type `git config --global user.name`. The command must print your name.
2. Type `git config --global user.email`. The command must print your email address.
3. If a command prints nothing, type the same command again with the value in quotes, for
   example `git config --global user.name "Your Name"`.
4. The first `git push` at stage 9 asks you to sign in to GitHub. A browser window opens.
   Click **Authorize**. Type nothing in the terminal. This works only in the terminal
   inside VS Code.

### Step 6: the stage guide

1. You receive the file `stage-guide.html` before the session. Save it in the folder
   `ai-chatbot`, next to `check.py`.
2. This page is the worksheet for each stage. `.gitignore` keeps the page out of your
   pushes.

### Step 7: the OpenCode tutor

1. In the same terminal (WSL for Windows), type `opencode --version`. The number must start
   with 2, for example `opencode v2.2.5`.
2. If OpenCode is not installed, or the number starts with 1, type this one command:
   `curl -fsSL https://opencode.ai/v2/install | bash -s -- --version 2.2.5`
   The command replaces an older OpenCode. Do not use the Download buttons on opencode.ai.
   Those buttons install a desktop app that the course does not use.
3. Type `opencode` at this folder one time. Connect the Google provider to your Gemini key.
   The tutor runs on Gemini. If Gemini refuses, type `/models` inside OpenCode and select a
   different model.
4. `ask-the-tutor.md` in this folder lists the questions to ask the tutor at each stage.

### Step 8: the virtual environment and the check

Type one command at a time, at this folder:

1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python check.py`

`check.py` makes `.env` and prints one line for each item that it found. If a line tells you
what to correct, correct it and type `python check.py` again. Post a screenshot of the lines
in the class channel two days or more before the session. Paste your key into `.env` only
when the session tells you to.

The virtual environment is on only in the terminal where you switched it on. It stays on
until you close that terminal. The prompt starts with `(.venv)` while it is on. In each new
terminal tab, type `source .venv/bin/activate` before the first `python` command. Without
it, macOS answers "command not found: python". WSL answers "No module named openai" or
"No module named flask".

## The four blocks

| Block | Stages | Run |
|---|---|---|
| Base | 1 to 6 | `python 01_base/stage1.py` … `python 01_base/stage5.py`; stage 6 changes `.env` only; the steps are in `01_base/stage6.md` |
| Web interface | 7 to 8 | `python 02_web/stage7/app.py` then `python test_chat.py`; `python 02_web/stage8/app.py` then open http://localhost:8000; five modifications in `02_web/stage8/modifications.md` |
| Deploy | 9 | the root files `app.py`, `index.html` and `test_chat.py`; the steps are in `03_deploy/README.md` |
| Customise | 10 | see `04_customise/MODIFY.md` |

Open `stage-guide.html` in your browser: it is the worksheet for every stage, with the
learning moment, the mental model, the new lines and the predict question with a reveal.

Each stage script starts with a header that says what the stage adds, why, and the question
to predict before you run. The lines marked `NEW in stage N` are the only lines that changed
from the previous stage. The script pauses once for your prediction, then runs.
