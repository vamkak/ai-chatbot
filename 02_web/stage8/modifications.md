# Five modifications to stage 8

Each modification below changes `02_web/stage8/app.py`. Each one is a habit that real
applications keep: measure the cost, limit the cost, check the input, serve a single-turn
tool, and do not wait without a limit. Do the modifications in order, one at a time. Each
one is between one and eight lines.

For each modification, write your prediction before you run. Then test with the page at
http://localhost:8000 and with `python test_chat.py` in a second terminal. The prompt of
each terminal must show `(.venv)`. The three tests, behaviour, memory and budget, must pass
after each modification, except where the text says otherwise.

The labels below are the numbered comments in `app.py`, for example `# 6. Call the model`.
The tutor can explain each line. The tutor does not write the change for you.

## 1. Print the tokens number in the terminal of the server

A real application records the tokens of each request, because the tokens are the bill.
Here the record is one printed line.

- Under label 7, after the line that sets `tokens`, add one `print`. The `print` shows the
  words `tokens sent:` and the value of `tokens`, in the same form as stage 4.
- Predict: which terminal will show the line, the server or the test client? Will the page
  change?
- Test: send three turns from the page and look at terminal 1. The number increases with
  the list, as in stage 4. The page does not change.
- The mistake to expect: the `print` is above the line that sets `tokens`. This gives a
  `NameError`. The `/error` command of the tutor reads it with you.

## 2. Limit the length of the reply with `max_tokens`

A real application sets a limit on each call. Then one request cannot run to the maximum of
the model. The limit bounds the cost and the wait time. The same limit keeps the answers
short.

- Under label 6, inside the `create(` call, add one argument on its own line: `max_tokens`
  set to a small number, for example 40. Put a comma after it, as in `messages=messages,`.
- Predict: will the tokens number sent change, or only the reply?
- Test: ask the café a question that needs a long answer. The reply stops before the end.
  The tokens number sent is the same as before, because the limit applies to the reply, not
  to the request. Increase the number until the memory test passes again.
- The mistake to expect: a limit so small that the reply to turn 2 stops before it says
  Sunday. Then the memory test fails for a reason that is not memory. On some free models
  the reply is empty at each small limit, and the page shows "null". The model uses the
  full limit for hidden reasoning before it writes. Test this modification on Gemini.
  There, a limit of 20 gives a cut reply of approximately twelve words.

## 3. Refuse a message that is too long before the call to the model

A real application checks the input at the boundary before it pays for a call. A public
address that forwards all input to a paid model is open to oversized input and hostile
input. A length check is the first guard. A rate limit is the second guard.

- Under label 4, after the line that reads `history`, read the content of the last entry.
  `history[-1]["content"]` is the text that the visitor typed.
- Add a check in the shape of the passphrase check of stage 9. If the length of that text,
  `len(...)`, is more than 300, return a dictionary. The dictionary has a readable reply,
  for example "Your message is over 300 characters. Please shorten it.", and the tokens
  value `"unknown"`. After the dictionary, return the status number 400. Status 400 is a
  bad request.
- Predict: what will the page show? What will the log line of the server say instead of
  200?
- Test: paste a long paragraph into the page. The reply is your sentence. The log line ends
  in 400. The program did not call the model. A normal message still gets 200.
- The mistake to expect: the check is under label 5 instead of label 4, after the program
  added the system entry. `history[-1]` is still correct, but the check runs later than
  necessary. The check works, but the goal is to refuse before the program does any work.

## 4. Add a single-turn route, `POST /summarise`

Most single-turn AI tools are a fixed instruction plus one user input, with no history.
Summarisers, classifiers, extractors and rewriters are examples. The only difference from a
chatbot is this: a chatbot sends a list.

- Below the chat route, copy labels 4 to 7 as a second function. Put a new route line above
  it: `@app.post("/summarise")`. Give the function a new name.
- Change three things in the copy. First, read `text` from the body instead of `history`.
  Second, build `messages` as two entries: a system entry with the content "Summarise the
  text you are given in two sentences", and one user entry with the text as its content.
  Third, return the reply under the key `"summary"`.
- Predict: how many entries does this route send to the model, for a conversation of any
  length on the page?
- Test: copy `test_chat.py` to `test_summarise.py`. Change `ADDRESS` so that it ends in
  `/summarise`. Replace the loop with one `requests.post` that sends `{"text": ...}` with a
  paragraph of your choice. Print `answer["summary"]`. Then run `test_chat.py` again. The
  chat route still passes, because nothing in it changed.
- The mistake to expect: the new route sends the system entry of the café. Then the
  summariser refuses each text that is not about the café. Each route has its own
  instruction.

## 5. Set a timeout on the call to the model

A real application never waits for a provider without a limit. On Vercel, a function that
waits too long stops with no message. A timeout turns that stop into a readable reply.

- Under label 6, inside the `create(` call, add the argument `timeout` set to 20. The unit
  is seconds. Put the argument on its own line with a comma, like the `max_tokens` line.
- Predict: when the provider is slow, which message will the page show? Which line in
  `app.py` sends that message?
- Test: set the timeout to a very small number, for example 0.01, and send one turn. The
  call fails before the provider answers. The `except APIError` block under label 6 catches
  the failure. The page shows "The provider refused the request", with the timeout named in
  the text. Set the timeout back to 20. The three tests pass again.
- The mistake to expect: `timeout` is on the `OpenAI(` client under label 1, not on the
  call. That also works, and it applies to each call. The goal here is to see which line
  answers when the wait is too long.

## After the five

Run `python test_chat.py` one last time against the server with all five changes. The
memory test passes. The log shows 200 for the four turns. `app.py` is approximately fifteen
lines longer than stage 8. A deployed application needs those fifteen lines. The stages of
the course leave them out on purpose: they are habits, not lessons.
