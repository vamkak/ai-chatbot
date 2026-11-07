"""Stage 4: the history list is the memory, and the program sends all of it every
time.

What this stage adds: the list is created once, before the loop. Every typed turn
and every reply is appended to it. The whole list is sent on every call, and the
number of tokens sent is printed. A token is a piece of text that the provider
counts and charges for.
Why: this is what memory is. The model still keeps nothing.
"""
import os
from dotenv import load_dotenv
from openai import OpenAI, APIError

# 1. Connect to the provider.
load_dotenv()
client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
)

# 2. The system entry, unchanged.
system_entry = {
    "role": "system",
    "content": (
        "You are the assistant of a small café by the sea. "
        "Facts: it opens from 8 in the morning to 6 in the evening from Tuesday to Sunday, "
        "and it is closed on Mondays. It serves coffee, tea and cakes. "
        "Rule 1: answer in at most two sentences. "
        "Rule 2: answer only questions about the café; for anything else, reply exactly: "
        "I can only help with questions about the café."
    ),
}

# NEW in stage 4
# 3. Create the list once, outside the loop. This list is the memory.
history = [system_entry]

# 2b. The memory test: type these three turns in this order, then type quit.
print("Goal: see the memory work. The list is kept and sent whole. Type the three turns below in this order; turn 2 should name Sunday, and turn 3 should refer to the visit or the group.")   # NEW in stage 4
print("Memory test, turn 1: I plan to visit on Sunday with two friends. Do you serve tea?")
print("Memory test, turn 2: Will you be open on the day I mentioned?")
print("Memory test, turn 3: Will you have enough tea and cakes for all of us on that day?")   # NEW in stage 4
input("Predict first: will turn 3 refer to the Sunday visit or the group of three, and will the tokens number grow? Write it down, then press Enter only.\n")
turn = 0   # counts the turns, so that the script can speak after the last test turn

while True:
    question = input("You: ")
    if question == "quit":
        break

    # 4. The typed turn joins the list.   # NEW in stage 4
    history.append({"role": "user", "content": question})

    # 5. Send the whole list, every time.   # NEW in stage 4
    try:
        response = client.chat.completions.create(
            model=os.getenv("LLM_MODEL"),
            messages=history,
        )
    except APIError as refused:
        print("The provider refused the request:", refused)
        print("Check the three LLM values in .env on your laptop, or in Environment Variables in your Vercel project settings. If the message says rate limit, wait one minute and run again.")
        history.pop()   # take the unanswered question back out of the list
        continue

    # NEW in stage 4
    # 6. The reply joins the list too; print it with the number of tokens sent.
    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    tokens = response.usage.prompt_tokens if response.usage else "unknown"
    print("Bot:", reply)
    print("tokens sent:", tokens)
    turn = turn + 1
    if turn == 3:   # NEW in stage 4
        print("That was turn 3. Compare the three replies and the three tokens numbers with your prediction, then type quit.")

