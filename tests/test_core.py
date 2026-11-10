"""Example tests for QuestForge. Two small tests to copy from in Lesson 12."""

import unittest

from features import core, reports


class TestCore(unittest.TestCase):
    def test_move_follows_an_exit(self):
        data = {"rooms": {
            "entrance": {"description": "A cold entrance hall.", "exits": {"north": "library"}},
            "library": {"description": "Dusty shelves.", "exits": {"south": "entrance"}},
        }}
        self.assertEqual(core.move(data, "entrance", "north"), "library")
        self.assertEqual(core.move(data, "entrance", "west"), "entrance")

    def test_describe_returns_description(self):
        room = {"description": "A cramped kitchen.", "exits": {}}
        self.assertEqual(core.describe(room), "A cramped kitchen.")

    def test_exits_report_counts_exits_per_room(self):
        data = {"rooms": {
            "entrance": {"description": "A cold entrance hall.", "exits": {"north": "library", "east": "courtyard"}},
            "library": {"description": "Dusty shelves.", "exits": {"south": "entrance"}},
            "courtyard": {"description": "A stone courtyard.", "exits": {}},
        }}
        self.assertEqual(reports.exits_report(data), {
            "entrance": 2,
            "library": 1,
            "courtyard": 0,
        })

    def test_exits_report_handles_empty_world(self):
        self.assertEqual(reports.exits_report({"rooms": {}}), {})
    #Copilot assisted with wrting comprehensive test function by explaining structure
    def test_neighbors_returns_destinations_and_handles_dead_end(self):
        data = {"rooms": {
            "entrance": {
                "description": "Entrance.",
                "exits": {"north": "library", "east": "kitchen"},
            },
            "library": {"description": "Library.", "exits": {}},
            "kitchen": {"description": "Kitchen.", "exits": {}},
        }}

        self.assertEqual(
            core.neighbors(data, "entrance"),
            ["library", "kitchen"],
        )
        self.assertEqual(core.neighbors(data, "library"), [])


if __name__ == "__main__":
    unittest.main()
