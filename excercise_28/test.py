"""Module to test the functions"""

import unittest
from main import get_max


class TestMaxFunction(unittest.TestCase):
    def test_right_cases(self):
        self.assertEqual(get_max([1,2,3,4,5]), 5)
        self.assertEqual(get_max([1,2,3,40,5]), 40)
        self.assertEqual(get_max([1,200,3,40,5]), 200)
        self.assertEqual(get_max([10000,200,3,40,5]), 10000)

    def test_wrong_cases(self):
        self.assertNotEqual(get_max([1,2,3,4,5]), 53)


if __name__ == "__main__":
    unittest.main()
