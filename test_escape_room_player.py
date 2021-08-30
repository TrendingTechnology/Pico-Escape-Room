# UNITTEST
# --------
# import unittest
# unittest.main('test_escape_room_player')

# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

import unittest

from escape_room_player import EscapeRoomPlayer
from file_manager import FileManager


class TestEscapeRoomPlayer(unittest.TestCase):
    def setUp(self):
        """
        setUp class
        """
        # Instantiate
        self.player = EscapeRoomPlayer()
        self.file_manager = FileManager()

    def test_pick_up_red_key(self):
        """
        test pick_up_red_key functionality
        """
        # Params
        file_manager = self.file_manager

        # Returns
        return_1 = 'You picked up the red key!'

        # Calls
        string_1 = self.player.pick_up_red_key(file_manager)

        # Asserts
        self.assertEqual(string_1, return_1)

    def test_without_red_key(self):
        """
        test without_red_key functionality
        """
        # Returns
        return_1 = 'You do not have the red key to escape.'

        # Calls
        string_1 = self.player.without_red_key()

        # Asserts
        self.assertEqual(string_1, return_1)


if __name__ == '__main__':
    unittest.main()
