# Write a new area

**Difficulty:** S

## Description

The world is small. Add a new area: at least two new connected rooms with
descriptions, reachable from an existing room, so players have somewhere new
to explore.

## Acceptance criteria

- [ ] At least two new rooms are added to `data/questforge.json`, each with a
      description and exits.
- [ ] The new area connects to the existing map (an exit leads in, and back).
- [ ] `python main.py` can reach and look around every new room.
- [ ] No existing room's exits are broken by the change.

## Notes

This is a content-only ticket - no code changes needed, just careful JSON.
Touches `data/questforge.json`.
