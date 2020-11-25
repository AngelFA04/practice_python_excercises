"""Module to test the functions"""

import unittest
from main import select_winner


class TestGames(unittest.TestCase):
    def test_winners_outcomes(self):
        """Evualate select_winner outcomes"""
        self.assertEqual(select_winner('ROCK', 'PAPER'), 'Player 2')
        self.assertEqual(select_winner('PAPER', 'ROCK'), 'Player 1')

        self.assertEqual(select_winner('SCISSORS', 'PAPER'), 'Player 1')
        self.assertEqual(select_winner('PAPER', 'SCISSORS'), 'Player 2')

        self.assertEqual(select_winner('ROCK', 'SCISSORS'), 'Player 1')
        self.assertEqual(select_winner('SCISSORS', 'ROCK'), 'Player 2')


if __name__ == "__main__":
    unittest.main()
