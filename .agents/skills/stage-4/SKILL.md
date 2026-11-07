---
name: stage-4
description: Course notes for stage 4 of the chatbot course (01_base/stage4.py): what the stage adds, the predict question, the expected behaviour and the common fixes. Load when the learner asks about stage 4 or about 01_base/stage4.py.
metadata:
  opencode/autoinvoke: "true"
---
# Stage 4: 01_base/stage4.py

## What this stage adds

The list is created once before the loop; each typed turn and each reply is appended; the whole list is sent every call; the number of tokens sent is printed.

## Two lines a learner often asks about

- `history = [system_entry]` sits above the loop, so the list is created once and keeps growing. The same line inside the loop would create it again on every turn, which is stage 3.
- `history.append({"role": "assistant", "content": reply})` puts the model's own reply into the list, so on the next turn the model receives what it said as well as what the learner typed.

## The predict question

Will the reply to turn 3 refer to the Sunday visit or the group of three? Will the tokens number on turn 3 be bigger than on turn 1?

## What the learner should see

The script prints a goal line first: the list is kept and sent whole, turn 2 should name Sunday, and turn 3 should refer to the visit or the group. After turn 3 it asks the learner to compare the replies and the tokens numbers with the prediction. Turn 2 names Sunday. The tokens number grows every turn (about 104, then 120 to 140, then 160 to 180 on the current model) because the whole list, replies included, is resent. Turn 3 refers to the Sunday visit or to the group of three, facts that are only in turn 1.

## Common messages and what they mean

- 'I can only help with questions about the café.' as the reply to 'what was my last question?' is rule 2 refusing a question that is not about the café. It does not mean memory failed. Test memory with the three fixed turns, which ask about the café in a way only turn 1 can answer.
- 'tokens sent: unknown' means the provider did not return a usage count; the memory test still runs.
- If the number stays flat while the list grows, the call is not sending the list: see the Investigate questions for stage 4 on the stage guide page.
