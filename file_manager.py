# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false


class FileManager:
    """
    Class to implement file access to store config if
    power lost or reset to maintain persistence
    """

    @staticmethod
    def write_status_file(current_room_number):
        """
        Method to write the current room number achieved after answering the
        questions associated to open the door

        Params:
            current_room_number: int
        """
        try:
            with open('current_room_number', 'w') as file:
                file.write(current_room_number)
        except OSError:
            pass

    @staticmethod
    def read_status_file():
        """
        Method to read the current room number achieved after answering the
        questions associated to open the door
        """
        try:
            with open('current_room_number', 'r') as file:
                current_room_number = file.read()
                return current_room_number
        except OSError:
            pass

    @staticmethod
    def clear_status_file():
        """
        Method to clear status file after winning a game
        """
        try:
            with open('current_room_number', 'w') as file:
                file.write('')
        except OSError:
            pass

    @staticmethod
    def write_inventory_file(inventory_item):
        """
        Method to write inventory item to inventory file upon picking it up
        """
        try:
            with open('inventory', 'w') as file:
                file.write(inventory_item)
        except OSError:
            pass

    @staticmethod
    def read_inventory_file():
        """
        Method to read inventory file and return its contents

        Return:
            str
        """
        try:
            with open('inventory', 'r') as file:
                inventory = file.read()
                return inventory
        except OSError:
            pass

    @staticmethod
    def clear_inventory_file():
        """
        Method to clear inventory file after winning a game
        """
        try:
            with open('inventory', 'w') as file:
                file.write('')
        except OSError:
            pass
