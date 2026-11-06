"""Reference tests for the average_rooms feature (Lesson 12 answer key)."""

import unittest

from features import reports


class TestAverageRooms(unittest.TestCase):
    def test_empty_history_is_zero(self):
        self.assertEqual(reports.average_rooms({"history": []}), 0.0)

    def test_single_entry(self):
        self.assertEqual(reports.average_rooms({"history": [7]}), 7.0)

    def test_several_entries_are_averaged(self):
        self.assertEqual(reports.average_rooms({"history": [2, 3, 4]}), 3.0)


if __name__ == "__main__":
    unittest.main()
