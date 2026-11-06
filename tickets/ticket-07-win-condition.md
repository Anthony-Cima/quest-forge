# Add a win condition

**Difficulty:** S

## Description

Right now the game never ends - the player can only quit. Give the world a
goal room, so reaching it declares victory.

## Acceptance criteria

- [ ] A new function checks whether the current room is the world's goal room.
- [ ] Moving into the goal room prints a win message.
- [ ] The world file records which room key is the goal.
- [ ] A test covers reaching the goal room and not reaching it.

## Notes

Touches `data/questforge.json`, `features/core.py`, and `main.py`.
