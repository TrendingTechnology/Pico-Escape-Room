from time import sleep


class Music:
    """
    Class to handle a PWM music on a passive buzzer
    """

    def __init__(self, quarter_note=0.5, dotted_quarter_note=0.75, eighth_note=0.25, half_note=1.0, whole_note=2.0):
        """
        Attrs:
            quarter_note: float, optional
            dotted_quarter_note: float, optional
            eighth_note: float, optional
            half_note: float, optional
            whole_note: float, optional
        """
        self.quarter_note = quarter_note
        self.dotted_quarter_note = dotted_quarter_note
        self.eighth_note = eighth_note
        self.half_note = half_note
        self.whole_note = whole_note
        self.notes = {
            'E3': 164.81,
            'G3': 196.00,
            'A4': 440.00,
            'Ab4': 415.30,
            'C4': 261.63,
            'D4': 293.66,
            'E4': 329.63,
            'F4': 349.23,
            'G4': 392.00,
            'C5': 523.25,
            'E5': 659.25,
            'F5': 698.46,
            'G5': 783.99
        }

    @staticmethod
    def play(pwm, note, note_duration):
        """
        Method to play a note

        Params:
            pwm: object
            note: str
            note_duration: float
        """
        try:
            pwm.freq(int(note))
            pwm.duty_u16(512)
            sleep(note_duration)
            pwm.deinit()
        except ValueError:
            return False
