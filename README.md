# QuestForge

A tiny text-adventure engine you run in the terminal. The story lives in a
JSON world file - move between rooms and look around.

## Run it

```bash
python main.py
```

## Run the tests

```bash
python -m unittest
```

Both commands work from the root of this repo with no setup and no installs.

## What is in here

| Path | What it does |
|---|---|
| `main.py` | The menu loop you interact with |
| `storage.py` | Loads and saves the JSON data file |
| `features/core.py` | The world, moving between rooms, and small helpers |
| `features/reports.py` | Summary reports - Featuring a new exit report (v2.0) |
| `data/questforge.json` | The room graph and move history |
| `tests/test_core.py` | Example tests to copy from |
| `tickets/` | The eight tickets your squad works through |
| `docs/README.md` | The product guide, plus the Team list you add yourself to |
| `CONTRIBUTING.md` | The Definition of Done and the branch naming rules |

## Before you open your first pull request

Read **[CONTRIBUTING.md](CONTRIBUTING.md)**. A pull request is done only when
all five are true: the ticket is linked, it runs, a squadmate reviewed it, a
test covers it, and the docs reflect the change. Never commit straight to
`main` - it is what a new teammate clones and what the demo runs from.

## Team

- Anthony Cima (Project head, Lead coder)