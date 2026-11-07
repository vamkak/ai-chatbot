# Stage 10: make the chatbot your own

## The Modify menu

Do the six steps below in this order. Each step is required.

1. In `app.py`, write a new system entry for a purpose of your own. Write who the assistant is, the facts it can use, and two rules.
2. In `index.html`, change the title and the greeting.
3. In `test_chat.py`, write your own three memory turns. Put a fact in turn 1. Put a question in turn 3 that needs that fact.
4. Run the app on your laptop one time. Type `python app.py` in terminal 1. Type `python test_chat.py` in terminal 2. The prompt of each terminal must start with `(.venv)`.
5. Commit and push. In Vercel, open Settings, then Environment Variables. Change the three LLM values to your OpenRouter block, with a model name that ends in `:free`. Click Save. Then click Redeploy on the Deployments page, as in `03_deploy/README.md`. A free model permits 20 requests each minute and 50 each day on an account with no credits. That is sufficient for this exercise.
6. Post your link in the class channel with a note of three sentences. Write what you changed, what you kept, and why the lines that you kept must not change.

After the session, you can do more. These changes are optional:

- Add a language rule.
- Make KEEP larger or smaller.
- Save the conversation to a file on your laptop.
- Replace the dropped turns with a summary.

## The reusable-code map

| File | Lines to change | Lines to keep |
|---|---|---|
| app.py | The system entry; the KEEP number | The client lines; the chat route; the trim line; the passphrase check; the refused-request lines; the run lines |
| index.html | The title; the greeting; the style lines | The array; the post; the two appends; the passphrase prompt |
| .env and Vercel's settings | The provider's three values; the passphrase | The names of the four values |
| test_chat.py | The turns | The loop; the post; the appends |
