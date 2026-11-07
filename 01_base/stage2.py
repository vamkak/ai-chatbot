"""Stage 2: the system entry is the first entry in the list, and it is code.

What this stage adds: a system entry at the top of the list, and the three fixed
questions of the behaviour test, each sent in its own call.
Why: the entry is the only thing the model knows about the café, and it goes on
every call.
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

# NEW in stage 2
# 2. Write the system entry: who the assistant is, what it knows, and its rules.
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

# 3. The three fixed questions of the behaviour test.   # NEW in stage 2
TEST_QUESTIONS = [
    "What time do you open on Sundays?",
    "What is the capital of France?",
    "Tell me everything about your menu.",
]

print("Goal: see the system entry at work. Question 1 should be answered from the facts, question 2 refused, and question 3 answered in at most two sentences.")   # NEW in stage 2
input("Predict first: what will the reply to question 2 do? Write it down, then press Enter only.\n")

# NEW in stage 2
# 4. Send each question in its own call, with the system entry first every time.
for question in TEST_QUESTIONS:
    messages = [system_entry, {"role": "user", "content": question}]
    try:
        response = client.chat.completions.create(
            model=os.getenv("LLM_MODEL"),
            messages=messages,
        )
    except APIError as refused:
        print("The provider refused the request:", refused)
        print("Check the three LLM values in .env on your laptop, or in Environment Variables in your Vercel project settings. If the message says rate limit, wait one minute and run again.")
        continue

    # 5. Print the question and the reply.
    reply = response.choices[0].message.content
    print("You:", question)
    print("Bot:", reply)

# 6. The three checks of the behaviour test.   # NEW in stage 2
print("Check: was question 1 answered from the facts, question 2 refused with the exact sentence, and question 3 answered in at most two sentences?")
