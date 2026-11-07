---
name: stage-0
description: Course notes for stage 0 of the chatbot course (check.py): what the stage adds, the predict question, the expected behaviour and the common fixes. Load when the learner asks about stage 0 or about check.py.
metadata:
  opencode/autoinvoke: "true"
---
# Stage 0: check.py

## What this stage adds

Create .env on the first run and check Python, the folder, the packages and the key.

## The predict question

At home, before the key is pasted, which line will the script print last?

## What the learner should see

At home: the line that .env was created, the Python, folder and packages lines, then the line 'LLM_API_KEY is not set yet'. In the session, after the key is pasted: 'Your laptop is ready. Models available: models/gemini-3.5-flash-lite, ...'. The model names carry a models/ prefix; the name written into .env is the part after the slash.

## Common messages and what they mean

- 'the virtual environment is not on' means the Python that ran is not the one in .venv, often the Python of another tool such as conda. Run source .venv/bin/activate, then python check.py again.
- 'too old. The course needs Python 3.10 or newer' means the Python in the virtual environment is older than 3.10.
- 'this is the Windows side' means the repository is under /mnt/c/; it must be in the WSL home folder.
- 'You are running Windows Python' means the folder was not opened in WSL.
- 'Package missing' means the virtual environment is not active, or pip install -r requirements.txt was not run.
- 'The provider refused the key' means the key in .env does not match the AI Studio page.
