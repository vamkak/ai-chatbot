"""The three fixed tests as one command. This is a test tool; it is not part of the
chatbot.
Terminal 1 runs the server. Terminal 2 runs this script: python test_chat.py.
"""
import requests

# 1. Where the requests go. Stage 9: change this to your Vercel link followed
#    by /chat.
ADDRESS = "http://localhost:8000/chat"
PASSPHRASE = "choose-a-word"   # stage 9: the word you set as APP_PASSWORD

# 2. The four fixed turns: the three memory turns, then the behaviour question.
TURNS = [
    "I plan to visit on Sunday with two friends. Do you serve tea?",
    "Will you be open on the day I mentioned?",
    "Will you have enough tea and cakes for all of us on that day?",
    "What is the capital of France?",
]

# 3. The list. The caller keeps it; the server keeps nothing.
history = []

# 4. For each turn: the turn joins the list, the whole list is sent, the reply
#    joins the list.
print("Goal: the three tests through the route. Turn 2 should name Sunday, turn 3 should refer to the visit or the group, and the France question should get the refusal sentence.")
for turn in TURNS:
    history.append({"role": "user", "content": turn})
    answer = requests.post(ADDRESS, json={"history": history, "passphrase": PASSPHRASE}).json()
    history.append({"role": "assistant", "content": answer["reply"]})
    print("You:", turn)
    print("Bot:", answer["reply"], "| tokens sent:", answer["tokens"])

# 5. The checks.
print("Check: did turn 2 name Sunday, did turn 3 refer to the visit or the group, was the France question refused with the exact sentence, and did every tokens number stay under 300?")
