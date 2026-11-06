# Checkpoint - after Lesson 10 (Debugging I)

Reference "on-track" state. A student who fell behind can switch here to rejoin
from a known-good baseline; instructors use it as the worked answer key.

What should be true now:

- Both seeded logic bugs from `lesson/10-start` are fixed: `room_count` returns
  `len(data["rooms"])` (not `len(data["start"])`), and `exits_for` returns every
  exit key (not all-but-the-last).
- `features/core.py` now matches `main` - `main` is the correct reference.

`python -m unittest` passes.
