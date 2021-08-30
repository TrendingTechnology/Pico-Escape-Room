# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

import unittest

from file_manager import FileManager


class TestFileManager(unittest.TestCase):
    def setUp(self):
        """
        setUp class
        """
        # Instantiate
        self.file_manager = FileManager()

    def test_1_write_inventory_file(self):
        """
        test write_inventory_file functionality
        """
        # Params
        inventory_item = 'Red Key'

        # Returns
        return_1 = None

        # Calls
        none_1 = self.file_manager.write_inventory_file(inventory_item)

        # Asserts
        self.assertEqual(none_1, return_1)

    def test_2_read_inventory_file(self):
        """
        test write_inventory_file functionality
        """
        # Returns
        return_1 = 'Red Key'

        # Calls
        string_1 = self.file_manager.read_inventory_file()

        # Asserts
        self.assertEqual(string_1, return_1)

    def test_clear_inventory_file(self):
        """
        test clear_inventory_file functionality
        """
        # Returns
        return_1 = None

        # Calls
        none_1 = self.file_manager.clear_inventory_file()

        # Asserts
        self.assertEqual(none_1, return_1)


if __name__ == '__main__':
    unittest.main()
