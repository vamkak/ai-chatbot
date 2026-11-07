# Questions to ask the tutor at each stage

The tutor is OpenCode, started with the command `opencode` at the root of your repository.
It has read every file in the folder and the course notes for each stage. It answers
questions about Python and about the scripts directly, in short bullet points. Before it
tells you what a stage will print, it asks for your prediction once; if you write "just tell
me", it tells you. It explains errors and says the fix in words, and it never writes or
rewrites a stage, because the course keeps the writing with you.

Three commands cover most of what you will ask: `/explain` walks a stage file line by line,
`/quiz` asks you three predict-the-output questions before a run, and `/error` reads an
error message with you. You can also ask in plain words. The questions below are the ones
that teach the most at each stage; ask them in your own words, and ask any other question
that comes up.

## Stage 0: check.py

1. Explain check.py line by line.
2. Why does check.py make the .env file for me? Why do I not copy .env.example?
3. What does the line "the virtual environment is not on" mean? Why does each new terminal
   tab need the activate command again?
4. Where does my key go? Why is the key never written in the code?

## Stage 1: one call

1. Where is the code that connects to the model? What do the three values in it do?
2. What is a list in Python? Why is my message a dictionary inside a list?
3. Why do two runs give different replies, also with temperature set to zero?
4. What does `raise SystemExit` do when the provider refuses the request?
5. Quiz me on stage 1.

## Stage 2: the system entry

1. What is the difference between the system entry and the user entry? Why must the system
   entry be first in the list?
2. Show me the line that sends the three questions as three separate calls.
3. Why can the model break a rule that is written in the system entry?
4. If I change one sentence of the system entry, what changes in the replies?

## Stage 3: a loop without memory

1. What does `while True` do? How does the word quit stop it?
2. What does `input()` return? Where does that text go?
3. Which line builds the list again on each turn?
4. Why does the model not know which day I named when I ask turn 2?

## Stage 4: the list is the memory

1. Which line makes the list one time? Why is that line outside the loop?
2. What does `history.append` do? Why are there two appends?
3. Why does the tokens number increase on each turn?
4. Why is "what was my last question?" refused when the memory works?
5. What does `history.pop()` do when the provider refuses the request?

## Stage 5: KEEP trims the list

1. Explain `history[-KEEP:]` one piece at a time.
2. Why does the trim never remove the system entry?
3. Why does turn 2 sometimes still say Sunday when KEEP is 2?
4. Quiz me on stage 5 before I change KEEP.

## Stage 6: the provider is three values

1. Nothing in the code changed. What did change?
2. What does the base URL do? Why is it one of the three values?
3. What does a message with 429 or "rate limit" mean? What are the free limits?
4. Why do I switch .env back to Gemini after this stage?

## Stage 7: the route

1. Explain 02_web/stage7/app.py line by line.
2. What is a route? What is JSON?
3. What does the server keep between two requests? Where is the list?
4. Read this log line with me: "POST /chat HTTP/1.1" 200.
5. What does the WARNING line about a development server mean?

## Stage 8: the page keeps the list

1. Where is the list now? In which language is it written?
2. What does the fetch call in index.html send to the server?
3. Why is the list empty after a refresh of the page?
4. What is the line "GET /favicon.ico" 404 in the terminal of the server?
5. In modifications.md, which of the five changes change the call to the model? Which
   change the route around it?

## Stage 9: the passphrase and Vercel

1. The app is on Vercel. Where is the key?
2. What do the lines of the passphrase check do? What does status 401 mean?
3. Why is the passphrase a check and not a guarantee of security?
4. What does "This page is unavailable" with FUNCTION_INVOCATION_FAILED mean?
5. Read this error with me. Then paste the last lines that the page or the terminal
   showed.

## Stage 10: make the chatbot your own

1. Which lines in app.py can I use again for any chat application? Why?
2. How do I write a memory test for my own purpose? The test has a fact in turn 1 and a
   question in turn 3 that needs that fact.
3. Why does a change of the model on Vercel need no new push?
4. What makes a rule in a system entry testable? How do I test my rule?
