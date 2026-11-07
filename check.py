"""Stage 0: check that your laptop is ready.

What this stage adds: nothing to the chatbot yet. The script creates .env if it
is missing, then checks the Python version, the folder, the packages and the
key.
Why: every later stage assumes these four things are right. Every later stage
reads the same .env file, because the python-dotenv package looks for it in the script's folder
and in every folder above the script that runs.
"""
import os
import shutil
import sys
from pathlib import Path

# 1. Create .env on the first run, so that nobody copies or renames a file.
env_file = Path(__file__).with_name(".env")
if not env_file.exists():
    shutil.copy(env_file.with_name(".env.example"), env_file)
    print("I created .env for you, next to check.py. Open it and paste your key after LLM_API_KEY= when the session asks you to.")

# 2. The Python version, and whether it is the one in the virtual environment.
#    Inside a virtual environment, sys.prefix differs from sys.base_prefix.
version = sys.version.split()[0]
in_venv = sys.prefix != sys.base_prefix
if not in_venv:
    print("Python", version, "- the virtual environment is not on. Run: source .venv/bin/activate, then python check.py again.")
    sys.exit()
elif sys.version_info >= (3, 10):
    print("Python", version, "in the virtual environment - OK")
else:
    print("Python", version, "- too old. The course needs Python 3.10 or newer.")

# 3. The folder: on Windows, everything must be inside WSL.
folder = str(Path.cwd())
if sys.platform == "win32":
    print("You are running Windows Python. Open this folder in WSL and run the script there.")
elif folder.startswith("/mnt/c/"):
    print("Working folder:", folder, "- this is the Windows side. Clone into your WSL home folder.")
else:
    print("Working folder:", folder, "- OK")

# 4. The four packages. They are imported here, and not at the top, so that a
#    missing one gives this line and not a long error.
try:
    import flask, requests
    from dotenv import load_dotenv
    from openai import OpenAI, APIError
    print("Packages installed - OK")
except ImportError as missing:
    print("Package missing:", missing.name, "- run: pip install -r requirements.txt, then python check.py again.")
    sys.exit()

# 5. The key. The code reads it from .env; it is never written in this file.
load_dotenv(env_file)
key = os.getenv("LLM_API_KEY", "")
if not key or key.startswith("paste-"):
    print("LLM_API_KEY is not set yet. You will paste it into .env in the session. Nothing else to do now.")
    sys.exit()

# 6. One request that proves the key works: ask the provider for its model list.
client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=key,
)
try:
    names = [model.id for model in client.models.list()]
    print("Your laptop is ready. Models available:", ", ".join(names[:5]), "...")
except APIError as refused:
    print("The provider refused the key:", refused)
    print("Check LLM_API_KEY in .env against the key on your AI Studio page.")

