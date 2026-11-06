# Add a neighbors helper

**Difficulty:** S

## Description

Right now you can only look at exit names, not where they lead. Add a helper
that, given the world and a room key, returns the list of room keys reachable
directly from that room - handy for anything that needs to inspect the map
without walking it one step at a time.

## Acceptance criteria

- [ ] A new function `neighbors(data, room_key)` lives in `features/core.py`.
- [ ] It returns the list of destination room keys reachable from `room_key`.
- [ ] A room with no exits returns an empty list (no crash).
- [ ] A test in `tests/` covers a room with multiple exits and a dead end.

## Notes

Touches `features/core.py` and a test file. No changes to the data file needed.
