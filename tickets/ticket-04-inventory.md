# Add a player inventory

**Difficulty:** M

## Description

Adventures need loot. Let the player pick up named items and carry them from
room to room, and see what they're holding.

## Acceptance criteria

- [ ] A new function adds an item name to a running inventory list.
- [ ] A new function returns the current inventory (empty list if nothing yet).
- [ ] A new menu option in `main.py` lets the player pick up an item and see
      their inventory.
- [ ] A test covers adding an item and reading back an empty inventory.

## Notes

Keep the inventory in memory for now - it doesn't need to be saved to the data
file. Touches `features/core.py` and `main.py`.
