---
name: stage-6
description: Course notes for stage 6 of the chatbot course (.env): what the stage adds, the predict question, the expected behaviour and the common fixes. Load when the learner asks about stage 6 or about .env.
metadata:
  opencode/autoinvoke: "true"
---
# Stage 6: .env

## What this stage adds

No code change. The three provider values in .env are switched from the Gemini block to the OpenRouter block, and 01_base/stage5.py runs unchanged. The steps are in 01_base/stage6.md.

## The predict question

To run this chatbot on a different provider, what must change in the code?

## What the learner should see

Nothing in the code changes. With the OpenRouter lines active and a model name ending in :free, the same script runs on the free model. The replies may differ in tone and speed, the refusal rule may be weaker, and the tokens number may print as unknown. The free limits are 20 requests a minute and 50 a day without credits.

## Common messages and what they mean

- 'The provider refused the request' with 429 on the free model means the per-minute or per-day free limit; wait a minute or pick another :free model.
- If the model name is wrong, the provider's message says the model was not found; copy the name exactly from the model list.
- 'no upstreams available' with 503 means the company serving that free model has no capacity at the moment; choose another :free model and run again.
- An empty reply from a free model means it spent its words on hidden reasoning before answering; choose another :free model.
- Do not type personal or client information into a free model.
