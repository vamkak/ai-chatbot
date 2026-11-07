"""Stage 7: a web route answers one chat request.

What this stage adds: a web route. The caller sends the whole history in one
request and receives one reply.
What it removes: the loop, the typed input and the appends. The server keeps
nothing; the caller keeps the list.
"""
import os
from dotenv import load_dotenv
from openai import OpenAI, APIError
from flask import Flask, request   # NEW in stage 7

# 1. Connect to the provider.
load_dotenv()
client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
)

# 2. The system entry, unchanged. KEEP is 6, the value that passed all three
#    memory turns in stage 5.
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
KEEP = 6

# 3. Create the server.   # NEW in stage 7
app = Flask(__name__)

# NEW in stage 7
# 4. The chat route: the caller's list arrives in the request body.
@app.post("/chat")
def chat():
    history = request.get_json()["history"]

    # 5. Add the system entry and trim. The caller never holds the system
    #    entry; the server adds it.
    messages = [system_entry] + history[-KEEP:]

    # 6. Call the model. A refusal is returned as the reply, so the caller
    #    sees it.
    try:
        response = client.chat.completions.create(
            model=os.getenv("LLM_MODEL"),
            messages=messages,
        )
    except APIError as refused:
        reply = (
            "The provider refused the request: " + str(refused)
            + " Check the three LLM values in .env on your laptop, or in Environment Variables in your Vercel project settings. If the message says rate limit, wait one minute and run again."
        )
        return {"reply": reply, "tokens": "unknown"}

    # 7. Return one reply and the number of tokens sent. The server keeps
    #    nothing.
    reply = response.choices[0].message.content
    tokens = response.usage.prompt_tokens if response.usage else "unknown"
    return {"reply": reply, "tokens": tokens}

# NEW in stage 7
# 8. Running this file starts the server on your laptop. Vercel ignores these
#    two lines.
if __name__ == "__main__":
    app.run(port=8000, debug=True)

