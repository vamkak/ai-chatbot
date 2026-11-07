# Stage 9: deploy to Vercel

Stage 9 is the three files at the root of this repository: `app.py`, `index.html` and
`test_chat.py`. The files are at the root because Vercel runs the root. `app.py` is stage 8
plus the passphrase check. `index.html` is stage 8 plus the passphrase prompt. The lines
marked `NEW in stage 9` are the only lines that changed. The table "If something is wrong"
at the end of this page lists each message and error page that you can see. Look there
first.

## Why Vercel needs its own copy of the four values

`.gitignore` lists your `.env` file. Thus git never uploaded `.env` to GitHub, and Vercel
builds from GitHub. On Vercel, the same line `os.getenv("LLM_API_KEY")` reads the
environment settings of the project, not `.env`. The code does not change. The place that
the code reads the values from changes. Until you enter the four values there, the deployed
program cannot start or cannot answer. The fix table at the end of this page names each
case.

## Part 1: run it on your laptop first (5 minutes)

1. Open `.env` at the root. Change the last line, `APP_PASSWORD=choose-a-word`, to a word
   of your choice, for example `APP_PASSWORD=seaside`. Save the file.
2. In terminal 1, at the root, make sure that the prompt starts with `(.venv)`. If it does
   not, type `source .venv/bin/activate` first.
3. Type `python app.py`. Open http://localhost:8000 in the browser. Enter your passphrase
   when the page asks for it. Send one message. Stop the server with Ctrl+C.
4. In terminal 2, at the root, type `git status`. The file `.env` must not be in the list.
   If `.env` is in the list, stop. The `.gitignore` line is missing, and the next step
   would upload your key.
5. Type `git add .`, then `git commit -m "chatbot with passphrase"`, then `git push`.
6. If this is your first push, a browser window opens and asks you to sign in to GitHub.
   Click **Authorize** and go back to the terminal. If the terminal asks for a password,
   you are not in the terminal inside VS Code. Open the folder in VS Code and type
   `git push` again there.

## Part 2: put it on Vercel (10 minutes)

The labels below are the labels on the Vercel website in October 2026.

1. Sign in at https://vercel.com with the GitHub account of your repository.
2. Click **Add New**, then **Project**. In the list of your GitHub repositories, find
   `ai-chatbot`. Click **Import**.
3. On the import screen, keep the framework that Vercel detected (Flask). Keep the root
   directory as it is. Do not click Deploy yet.
4. Open the section **Environment Variables** on the same screen. Add the four values
   below one at a time: type the name in the **Key** box, type the value in the **Value**
   box, and click **Add**. Copy each value from your own `.env`. Type each name exactly as
   shown, with the underscores and in capitals.

   | Key | Value |
   |---|---|
   | `LLM_BASE_URL` | the address line from the active block of your `.env` |
   | `LLM_API_KEY` | your key from the same block |
   | `LLM_MODEL` | the model name from the same block |
   | `APP_PASSWORD` | the word you chose in Part 1 |

5. Click **Deploy**. The build takes approximately one to three minutes. When the build is
   complete, Vercel shows a preview and a **Visit** button.
6. Click **Visit**. The page asks for your passphrase. Enter it, then type the three memory
   turns. The first reply takes some seconds longer than the others, because Vercel starts
   the program for the first request. If you see "This page is unavailable" with the code
   FUNCTION_INVOCATION_FAILED, one of the three LLM values did not reach Vercel. Go to the
   next section.
7. Copy the link from the address bar of the browser. This is the link of the project, in
   the form `https://<project-name>.vercel.app`. Post this link and your passphrase in the
   class channel. Do not post the longer link with random letters. That link is one
   deployment only, and visitors who are not signed in to Vercel cannot open it.
8. In `test_chat.py`, change `ADDRESS` to your link followed by `/chat`. Change
   `PASSPHRASE` to the word from Part 1. At the root, with `(.venv)` in the prompt, type
   `python test_chat.py`.

## If you added the values after the first deploy

This section is also for the error page "This page is unavailable,
FUNCTION_INVOCATION_FAILED". The program stopped because a value is missing on Vercel.

1. Open your project on Vercel. Click **Settings**, then **Environment Variables** in the
   left menu. Add or edit the values as in Part 2, step 4. Click **Save**.
2. Click **Deployments** at the top. Open the menu with three dots on the most recent
   deployment. Click **Redeploy**. Only a new deployment reads a changed value.
3. If you need the error text of the program, open the deployment and click **Logs**. On
   the free plan, Vercel keeps the log for one hour. Look soon after the error.

## If something is wrong

| What you see | What it means | What to do |
|---|---|---|
| `command not found: python` (macOS) or `No module named flask` (WSL) | The virtual environment is not on in this terminal | Run `source .venv/bin/activate`, then the command again |
| The build fails | `requirements.txt` is missing or misspelled | Fix it, commit, push; Vercel builds again |
| Every reply is "APP_PASSWORD is not set on this server." | The value is missing in Vercel's settings | Add `APP_PASSWORD` in Settings, Environment Variables, then Redeploy |
| Every reply starts "The provider refused the request" | One of the three LLM values is wrong in Vercel's settings | Check the three names and values against your `.env`, then Redeploy |
| Every reply is "The passphrase is wrong." | The passphrase sent does not match `APP_PASSWORD` on the server | Compare three places and make them the same: the value on Vercel, the word the page asked for, and `PASSPHRASE` in `test_chat.py` |
| The page does not ask for a passphrase | An old build is open | Refresh after the new build finishes |
| A page that says "This page is unavailable" with a code like FUNCTION_INVOCATION_FAILED | One of the three LLM values is missing, so the program stopped at the line that creates the client | Add the missing value in Settings, Environment Variables, then Redeploy |
| `test_chat.py` says Connection refused, with localhost in the message | Before the deploy: the server in terminal 1 is not running. After the deploy: `ADDRESS` still points to localhost | Before the deploy, start `python app.py` in terminal 1. After the deploy, change `ADDRESS` to your link followed by `/chat` |

After the session, revoke both keys on the providers' pages and create new ones when you
next need them.
