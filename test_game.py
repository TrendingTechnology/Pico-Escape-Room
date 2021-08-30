# UNITTEST
# --------
# import unittest
# unittest.main('test_game')

# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

import unittest

from game import Game
from grid import Grid
from file_manager import FileManager


class TestGame(unittest.TestCase):
    def setUp(self):
        """
        setUp class
        """
        # Instantiate
        self.game = Game()
        self.grid = Grid()
        self.file_manager = FileManager()

    def test_correct_answer_response(self):
        """
        test correct_answer_response functionality
        """
        # Returns
        return_1 = 'Correct!'

        # Calls
        string_1 = self.game.correct_answer_response()

        # Asserts
        self.assertEqual(string_1, return_1)

    def test_incorrect_answer_response(self):
        """
        test incorrect_answer_response functionality
        """
        # Params
        correct_answer = '2014'

        # Returns
        return_1 = 'The correct answer is 2014.'

        # Calls
        string_1 = self.game.incorrect_answer_response(correct_answer)

        # Asserts
        self.assertEqual(string_1, return_1)

    def test_win(self):
        """
        test win functionality
        """
        # Params
        file_manager = self.file_manager

        # Returns
        return_1 = 'You Escaped!'

        # Calls
        string_1 = self.game.win(file_manager)

        # Asserts
        self.assertEqual(string_1, return_1)


if __name__ == '__main__':
    unittest.main()
