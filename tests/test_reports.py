import unittest

from features import reports


class TestReports(unittest.TestCase):
    def test_average_rooms_returns_average_rounded_to_one_decimal_place(self):
        data = {"history": [2, 3, 5]}

        self.assertEqual(reports.average_rooms(data), 3.3)

    def test_average_rooms_returns_zero_for_empty_history(self):
        data = {"history": []}

        self.assertEqual(reports.average_rooms(data), 0.0)


if __name__ == "__main__":
    unittest.main()
