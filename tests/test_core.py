"""Example tests for QuestForge. Two small tests to copy from in Lesson 12."""

import unittest

from features import core


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


if __name__ == "__main__":
    unittest.main()
