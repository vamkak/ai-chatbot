"""Stage 8: the page holds the history and the server holds nothing.

What this stage adds: one route that sends the page, index.html. The page keeps
the list in the browser and sends all of it on every turn.
What does not change: the chat route. The test client from stage 7 still passes.
"""
import os
from pathlib import Path   # NEW in stage 8
from dotenv import load_dotenv
from openai import OpenAI, APIError
from flask import Flask, request

# 1. Connect to the provider.
load_dotenv()
client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
)

# 2. The system entry and the limit, unchanged.
system_entry = {
    "role": "system",
    "content": (
        "You are the assistant of a small café by the sea. You are a sassy and fed up assistant that hates to reply."
        "Facts: it opens from 8 in the morning to 6 in the evening from Tuesday to Sunday, "
        "and it is closed on Mondays. It serves coffee, tea and cakes. "
        "Rule 1: answer in at most two sentences. "
        "Rule 2: answer only questions about the café; for anything else, reply exactly: "
        "I can only help with questions about the café."
    ),
}
KEEP = 6

# 3. Create the server.
app = Flask(__name__)

# NEW in stage 8
# 3a. The page route: send index.html, the file next to this one.
@app.get("/")
def page():
    return Path(__file__).with_name("index.html").read_text()

# 4. The chat route, unchanged.
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

# 8. Running this file starts the server on your laptop.
if __name__ == "__main__":
    app.run(port=8000, debug=True)

