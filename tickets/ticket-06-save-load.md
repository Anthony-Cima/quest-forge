# Save and load a game in progress

**Difficulty:** M

## Description

Right now every run starts back at the entrance. Let a player save which room
they're currently in and resume there next time they launch the game.

## Acceptance criteria

- [ ] A new menu option saves the current room key to disk.
- [ ] On startup, the game resumes from a saved room if one exists.
- [ ] With no saved game, the player starts at the normal starting room.
- [ ] A test covers saving a room and loading it back.

## Notes

`storage.save_data` / `storage.load_data` already handle the JSON file - decide
where a saved position should live in it. Touches `storage.py`, `main.py`, and
maybe `features/core.py`.
