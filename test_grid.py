# UNITTEST
# --------
# import unittest
# unittest.main('test_grid')

# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

import unittest

from grid import Grid
from escape_room_player import EscapeRoomPlayer


class TestGrid(unittest.TestCase):
    def setUp(self):
        """
        setUp class
        """
        # Instantiate
        self.grid = Grid()
        self.player = EscapeRoomPlayer()

    def test_create(self):
        """
        test create functionality
        """
        # Returns
        return_1 = ''
        return_2 = ''
        return_3 = ''

        # Calls
        string_1, string_2, string_3 = self.grid.create()

        # Asserts
        self.assertEqual(string_1, return_1)
        self.assertEqual(string_2, return_2)
        self.assertEqual(string_3, return_3)

    def test_update(self):
        """
        test update functionality
        """
        # Params
        self.player.dx = 0
        self.player.dy = 0
        player = self.player

        # Returns
        return_1 = ''

        # Calls
        string_1 = self.grid.update(player)

        # Asserts
        self.assertEqual(string_1, return_1)


if __name__ == '__main__':
    unittest.main()
