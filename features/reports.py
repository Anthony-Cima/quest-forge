"""Reporting helpers for QuestForge.

Heads up: this module is half-built on purpose. `world_summary` works, but
`exits_report` is still a stub with a clear seam to finish (see the tickets).
"""


def world_summary(data):
    return data["title"] + ": " + str(len(data["rooms"])) + " rooms"


def exits_report(data):
    # TODO(ticket): tally each room into a {room_key: number_of_exits} dict and return it.
    # For now this returns an empty report so the menu never crashes.
    report = {}
    return report
