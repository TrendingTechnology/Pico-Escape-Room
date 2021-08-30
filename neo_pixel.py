# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

import array
import time
import rp2


class NeoPixel:
    """
    Class to handle neo_pixel functionality
    """

    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 150, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    BLUE = (0, 0, 255)
    PURPLE = (180, 0, 255)
    WHITE = (255, 255, 255)
    COLORS = (BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE)

    def __init__(self, pin, led_count=64, brightness=0.5):
        """
        Attrs:
            pin: object
            led_count: int, optional
            brightness: float, optional
        """
        # Create the StateMachine with the ws2812 program, outputting on Pin(22)
        sm = rp2.StateMachine(0, self.__ws2812, freq=8_000_000, sideset_base=pin(22))
        # Start the StateMachine, it will wait for data on its FIFO
        sm.active(1)
        # Display a pattern on the LEDs via an array of LED RGB values
        ar = array.array('I', [0 for _ in range(led_count)])
        self.num_leds = led_count
        self.brightness = brightness
        self.sm = sm
        self.ar = ar

    @staticmethod
    @rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
    def __ws2812():
        """
        Internal method to handle ARM 32 assembly LED neo_pixel driver
        """
        T1 = 2
        T2 = 5
        T3 = 3
        wrap_target()
        label("bitloop")
        _ = out(x, 1).side(0)[T3 - 1]
        _ = jmp(not_x, "do_zero").side(1)[T1 - 1]
        _ = jmp("bitloop").side(1)[T2 - 1]
        label("do_zero")
        _ = nop().side(0)[T2 - 1]
        wrap()

    def clear_pixels(self):
        """
        Method to clear pixels
        """
        for i in range(self.num_leds):
            self.pixels_set(i, self.BLACK)
            self.pixels_show()

    def pixels_set(self, i, color):
        """
        Method to handle setting of pixels

        Params:
            i: int
            color: tuple
        """
        self.ar[i] = (color[1] << 16) + (color[0] << 8) + color[2]

    def pixels_show(self):
        """
        Method to handle illumination of pixels
        """
        dimmer_ar = array.array('I', [0 for _ in range(self.num_leds)])
        for i, c in enumerate(self.ar):
            r = int(((c >> 8) & 0xFF) * self.brightness)
            g = int(((c >> 16) & 0xFF) * self.brightness)
            b = int((c & 0xFF) * self.brightness)
            dimmer_ar[i] = (g << 16) + (r << 8) + b
        self.sm.put(dimmer_ar, 8)
        time.sleep_ms(10)

    def display(self, grid, grid_height, grid_width, led_count, process_grid):
        """
        Method to display grid

        Params:
            grid: object
            grid_height: int
            grid_width: int
            led_count: int
            process_grid: str
        """
        black = (0, 0, 0)
        red = (64, 0, 0)
        green = (0, 64, 0)
        index = 0
        for pixel in range(len(process_grid)):
            led = process_grid[index]
            if led == grid.led_on:
                # Turn on the wall led's of the top_wall+1 and the 1-bottom_wall
                if (0 <= index <= grid_width) or \
                        index >= (grid_width * grid_width - grid_width):
                    self.pixels_set(index, red)
                else:
                    # Turn on the player led at their current location
                    self.pixels_set(index, green)
                for _ in range(2, grid_height):
                    index_ = grid_height * _
                    # Turn on the right wall led's
                    self.pixels_set(index_-1, red)
                    # Turn on the left wall led's less the top two
                    self.pixels_set(index_, red)
            elif led == grid.led_off:
                # Available movable space less the current player location
                self.pixels_set(index, black)
            else:
                pass
            if index < led_count-1:
                index += 1
        self.pixels_show()
        time.sleep(0.25)

    def win_animation(self):
        """
        Method to display a win animation
        """
        for color in self.COLORS:
            for i in range(self.num_leds):
                self.pixels_set(i, color)
                time.sleep(0.01)
                self.pixels_show()
            time.sleep(0.2)
