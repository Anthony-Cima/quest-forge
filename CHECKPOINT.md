# Checkpoint - after Lesson 11 (Debugging II)

Reference "on-track" state. A student who fell behind can switch here to rejoin
from a known-good baseline; instructors use it as the worked answer key.

What should be true now:

- Both seeded exception bugs from `lesson/11-start` are fixed: `exits_by_room`
  reads the correct key `"exits"`, and `first_exit` indexes `0`.
- `features/core.py` now matches `main` - `main` is the correct reference.

`python -m unittest` passes.
