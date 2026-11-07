"""Stage 9: deploy to Vercel with the key in the environment and the link
protected.

What this stage adds: a passphrase check. The page asks the visitor for a
passphrase once and sends it with every request; the route answers only when it
matches APP_PASSWORD.
Why: the link is public, and anyone who finds it could spend your free
allowance.
"""
import os
from pathlib import Path
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

# 3a. The page route, unchanged.
@app.get("/")
def page():
    return Path(__file__).with_name("index.html").read_text()

# 4. The chat route. The body now holds the history and the passphrase.
@app.post("/chat")
def chat():
    data = request.get_json()   # NEW in stage 9

    # NEW in stage 9
    # 4b. The passphrase check. The passphrase is the fourth environment value.
    #     A missing value gets its own message, so that it is not read as a
    #     wrong passphrase.
    if not os.getenv("APP_PASSWORD"):
        reply = (
            "APP_PASSWORD is not set on this server. "
            + "Add it in .env on your laptop, "
            + "or in Environment Variables on Vercel."
        )
        return {"reply": reply, "tokens": "unknown"}, 401
    if data.get("passphrase") != os.getenv("APP_PASSWORD"):
        return {"reply": "The passphrase is wrong.", "tokens": "unknown"}, 401

    history = data["history"]   # NEW in stage 9

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

# 8. Running this file starts the server on your laptop. Vercel ignores these
#    two lines.
if __name__ == "__main__":
    app.run(port=8000, debug=True)

