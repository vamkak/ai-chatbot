# Stage 6: the provider is three values in .env

Stage 6 has no script of its own. The lesson is that nothing in the code changes when the
provider changes: you edit three lines in `.env` and run `01_base/stage5.py` again, this time
on an OpenRouter free model. The folder lists `stage1.py` to `stage5.py` for that reason.

## What to do

1. Open `.env` at the root. Put a `#` in front of the three active Gemini lines. Remove the
   `#` from the three OpenRouter lines. Exactly three lines must be without a `#`:

   ```text
   LLM_BASE_URL=https://openrouter.ai/api/v1
   LLM_API_KEY=paste-your-openrouter-key-here
   LLM_MODEL=paste-a-model-name-ending-in-:free
   ```

2. Paste your OpenRouter key after `LLM_API_KEY=`.
3. After `LLM_MODEL=`, type the name of a free model from https://openrouter.ai/models.
   The name ends in `:free`. Three models passed the tests at the last check of this
   course: `nvidia/nemotron-3.5-lightning:free`, `nvidia/nemotron-3.5-super-vl:free` and
   `liquid/lfm-2.5-2.6b:free`. A model can be gone when you read this. The test of a model
   is this: the refusal sentence comes back for the France question. Save the file.
4. At the root, with `(.venv)` in the prompt, type `python 01_base/stage5.py` again. Type
   the three memory test turns, then the France question. Tick the three tests on the
   stage guide page, as before.
5. When the tests are complete, put the `#` back in front of the three OpenRouter lines.
   Remove the `#` from the three Gemini lines. Then stages 7 to 9 run on Gemini. The
   OpenRouter block stays in the file for stage 10.

## What you should see

Nothing in the code changed, and the same script runs on a different provider. The replies
may differ in tone and speed, the refusal rule may be weaker, and the tokens number may
print as `unknown` if the provider does not return a count.

Free models have conditions: 20 requests a minute and 50 a day on an account that has
bought no credits, model names that are replaced without notice, and some that may train
on your prompts. Do not type personal or client information into a free model.

## If something is wrong

| What you see | What it means | What to do |
|---|---|---|
| "The provider refused the request" with 429 or "rate limit" | The per-minute or per-day free limit | Wait one minute, or choose another `:free` model |
| A message that the model was not found | The name after `LLM_MODEL=` is not exact | Copy the name again from the model list, including `:free` |
| "no upstreams available" with 503 | The company serving that free model has no capacity at the moment | Choose another `:free` model and run again |
| An empty reply, or a reply that starts with the model's own notes | That free model spends its words on hidden reasoning before it answers | Choose another `:free` model |
| "The provider refused the request" with 401 or "API key" | The OpenRouter key is wrong, or the Gemini lines are still active | Check the three lines without a `#` in `.env` |
| Four active lines, or two | A `#` is missing or one too many | Exactly three lines carry no `#`, all from one block |
