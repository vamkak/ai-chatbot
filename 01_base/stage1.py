"""Stage 1: one call returns one reply that differs on every run.

What this stage adds: the first call to the model, with a list that holds one
entry.
Why: every later stage is this call again, with a longer list.
"""
import os
from dotenv import load_dotenv
from openai import OpenAI, APIError

# 1. Connect to the provider. The three values come from .env, never from this
#    file.
load_dotenv()
client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL"),   # where the requests go
    api_key=os.getenv("LLM_API_KEY"),     # the account that is charged
)

# 2. Build the list. The model receives only what is in this list.
messages = [
    {"role": "user", "content": "Suggest one name for a small café by the sea and explain it in one sentence."},
]

input("Predict first: will a second run print exactly the same reply? Write it down, then press Enter only.\n")

# 3. Call the model, and handle the one error this stage teaches: a refused
#    request.
try:
    response = client.chat.completions.create(
        model=os.getenv("LLM_MODEL"),   # which model answers
        messages=messages,
        # temperature=0,   # remove the # for more similar replies
    )
except APIError as refused:
    print("The provider refused the request:", refused)
    print("Check the three LLM values in .env on your laptop, or in Environment Variables in your Vercel project settings. If the message says rate limit, wait one minute and run again.")
    raise SystemExit

# 4. Print the reply. The text is inside the response object.
reply = response.choices[0].message.content
print(reply)

