# Find the dead ends

**Difficulty:** M

## Description

Players get stuck without warning in rooms that have nowhere left to go. Add
a helper that, given the world, returns the room keys that are dead ends - rooms
with one exit or none at all.

## Acceptance criteria

- [ ] A new function `dead_ends(data)` lives in `features/core.py`.
- [ ] It returns a list of room keys whose room has one exit or zero exits.
- [ ] A room with two or more exits is never included.
- [ ] A world with no dead ends returns an empty list.
- [ ] A test in `tests/` covers a mixed world and the "no dead ends" case.

## Notes

Touches `features/core.py` and a test file. Think about looping over
`data["rooms"].items()` and checking exit counts.
