# Add NPCs with dialogue

**Difficulty:** M

## Description

Rooms feel empty without anyone in them. Let a room optionally hold an NPC
with a name and a line of dialogue, and let the player talk to whoever is in
the current room.

## Acceptance criteria

- [ ] Rooms can carry an optional `npc` entry with a name and a line.
- [ ] A new function returns the NPC in the current room (or `None`).
- [ ] A new menu option lets the player "talk" and see the NPC's line.
- [ ] Rooms with no NPC handle the "talk" option without crashing.
- [ ] A test covers a room with an NPC and a room without one.

## Notes

Start with one NPC in one room of `data/questforge.json` to prove it out.
Touches `data/questforge.json`, `features/core.py`, and `main.py`.
