"""Reporting helpers for QuestForge.

Heads up: this module is half-built on purpose. `world_summary` works, but
`exits_report` is still a stub with a clear seam to finish (see the tickets).
"""


def world_summary(data):
    return data["title"] + ": " + str(len(data["rooms"])) + " rooms"


def exits_report(data):
    report = {}
    for room_key, room in data.get("rooms", {}).items():
        report[room_key] = len(room.get("exits", {}))
    return report
