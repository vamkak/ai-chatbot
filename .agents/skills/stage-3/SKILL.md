---
name: stage-3
description: Course notes for stage 3 of the chatbot course (01_base/stage3.py): what the stage adds, the predict question, the expected behaviour and the common fixes. Load when the learner asks about stage 3 or about 01_base/stage3.py.
metadata:
  opencode/autoinvoke: "true"
---
# Stage 3: 01_base/stage3.py

## What this stage adds

A loop that takes a typed question each turn and builds the list again every turn, so there is no memory. Type quit to stop.

## The predict question

The script prints the two memory test turns before the gate; type them in order. What will the model say to turn 2, 'Will you be open on the day I mentioned?'

## What the learner should see

The script prints a goal line first: a list built again on every turn has no memory, and turn 2 should fail. After turn 2 it prints that a reply without Sunday is the designed failure and that stage 4 fixes it. Turn 2 is not answered for Sunday: the model asks which day, gives the opening times for every day, or gives the refusal sentence. All three are the same failure, because turn 1 is not in the list on turn 2. This is the designed failure.

## Common messages and what they mean

- If the prompt 'You:' does not appear, the script is still at the predict gate; press Enter.
- Typing quit ends the loop; pressing Ctrl+C prints a traceback, which is not an error in the script.
