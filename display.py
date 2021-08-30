# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

from utime import sleep
from sysfont import sysfont


class Display:
    """
    Class to handle a generic oled display
    """

    @staticmethod
    def clear(tft, oled):
        """
        Method proc to clear oled

        Params:
            tft: object
            oled: object
        """
        oled.fill(tft.BLACK)

    def text(self, tft, oled, text, wait=0, start_clear=False, end_clear=False):
        """
        Method to take a text str and display on the oled

        Params:
            tft: object
            oled: object
            text: str
            wait: int, optional
            start_clear: bool, optional
            end_clear: bool, optional
        """
        if start_clear:
            self.clear(tft, oled)
        oled.text((5, 5), text, tft.WHITE, sysfont, 1)
        sleep(wait)
        if end_clear:
            self.clear(tft, oled)

    def texts(self, tft, oled, text_1, text_2, text_3=None, text_4=None, wait=0):
        """
        Method to take a 4 text strings and display on the oled with a sleep

        Params:
            tft: object
            oled: object
            text_1: str
            text_2: str
            text_3: str, optional
            text_4: str, optional
            wait: int, optional
        """
        text_line_1 = text_1
        text_line_2 = text_2
        text_line_3 = text_3
        text_line_4 = text_4
        self.clear(tft, oled)
        oled.text((5, 5), text_line_1, tft.WHITE, sysfont, 1)
        sleep(wait)
        self.clear(tft, oled)
        oled.text((5, 5), text_line_2, tft.WHITE, sysfont, 1)
        sleep(wait)
        if text_3:
            self.clear(tft, oled)
            oled.text((5, 5), text_line_3, tft.WHITE, sysfont, 1)
            sleep(wait)
        if text_4:
            self.clear(tft, oled)
            oled.text((5, 5), text_line_4, tft.WHITE, sysfont, 1)
            sleep(wait)
        self.clear(tft, oled)
        oled.text((5, 5), 'Press Button 1, 2 or 3!', tft.WHITE, sysfont, 1)
