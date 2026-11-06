# Finish the exits report

**Difficulty:** S

## Description

`features/reports.py` has an `exits_report(data)` function that is only a stub -
it always returns an empty dict. Finish it so it counts how many exits each
room has. This is the report the menu's "Exit breakdown" option should
eventually use.

## Acceptance criteria

- [ ] `exits_report(data)` returns a dict of `{room_key: number_of_exits}`.
- [ ] Every room in the world is counted exactly once.
- [ ] An empty world returns an empty dict (no crash).
- [ ] A test in `tests/` checks the counts against a small sample world.

## Notes

Touches `features/reports.py` and a test file. The `exits_by_room` function
in `core.py` is a good reference for the tally pattern.
