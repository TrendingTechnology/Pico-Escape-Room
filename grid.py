# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

class Grid:
    """
    Class to represent a grid
    """

    def __init__(self, led_height=0, led_width=0, led_on='*', led_off=' '):
        """
        Attrs:
            led_height: int, optional
            led_width: int, optional
            led_on: int, optional
            led_off: int, optional
        """
        self.led_height = led_height
        self.led_width = led_width
        self.led_on = led_on
        self.led_off = led_off
        self.available_height = led_height - 2
        self.available_width = led_width - 2

    def create(self):
        """
        Method to create a grid

        Returns:
            str, str, str
        """
        top_wall = self.led_on * self.led_width
        side_walls = ''
        for _ in range(self.available_height):
            side_walls += self.led_on + self.led_off * self.available_width + self.led_on
        bottom_wall = self.led_on * self.led_width
        return top_wall, side_walls, bottom_wall

    def update(self, player):
        """
        Method to handle update with each event where we re-draw
        grid with player's current position

        Params:
            player: object

        Returns:
            grid: str
        """
        top_wall, side_walls, bottom_wall = self.create()
        grid = top_wall + side_walls + bottom_wall
        # Convert to a list so that the element can be mutable to add player char
        temp_grid = list(grid)
        # For each step in y, needs to increment by jumps of row width
        y_adjustment = (player.dy - 1) * self.led_width
        # The index position of player marker in the list-formatted grid
        position = self.led_width + player.dx + y_adjustment
        try:
            temp_grid[position] = self.led_on
        except IndexError:
            pass
        grid = ''
        grid = grid.join(temp_grid)
        return grid
