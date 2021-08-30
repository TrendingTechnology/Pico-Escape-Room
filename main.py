# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

from _thread import start_new_thread
from machine import Pin, SoftSPI, PWM
from st7735 import TFT
from game import Game
from data import questions
from grid import Grid
from file_manager import FileManager
from neo_pixel import NeoPixel
from escape_room_player import EscapeRoomPlayer
from display import Display
from music import Music

LED_COUNT = 64
GRID_WIDTH = 8
GRID_HEIGHT = 8
spi = SoftSPI(baudrate=2000000, polarity=0, phase=0, sck=Pin(2), mosi=Pin(1), miso=Pin(12))
oled = TFT(spi, 0, 3, 4)
oled.initb2()
oled.rgb(True)
btn_1 = Pin(7, Pin.IN, Pin.PULL_UP)
btn_2 = Pin(15, Pin.IN, Pin.PULL_UP)
btn_3 = Pin(21, Pin.IN, Pin.PULL_UP)
btn_4 = Pin(20, Pin.IN, Pin.PULL_UP)
pwm = PWM(Pin(5, Pin.OUT))
pwm.deinit()  # turn off sound on init
player_location = None
game = Game()
display = Display()
music = Music()
neo_pixel = NeoPixel(Pin)
grid = Grid(GRID_WIDTH, GRID_HEIGHT)
player = EscapeRoomPlayer()
file_manager = FileManager()
final_question = False
generate_random_location = True
random_location = None
previous_player_location = player_location
update_grid = grid.update(player)
response = None

display.clear(TFT, oled)

while True:
    # To ensure we do not generate a question if the player is hitting a wall
    # or not entering a valid move
    previous_player_location = player_location
    neo_pixel.display(grid, GRID_HEIGHT, GRID_WIDTH, LED_COUNT, update_grid)
    while True:
        if not btn_1.value():
            player_location = player.move_west(grid)
            update_grid = grid.update(player)
            break
        if not btn_2.value():
            player_location = player.move_east(grid)
            update_grid = grid.update(player)
            break
        if not btn_3.value():
            player_location = player.move_north(grid)
            update_grid = grid.update(player)
            break
        if not btn_4.value():
            player_location = player.move_south(grid)
            update_grid = grid.update(player)
            break
    if generate_random_location:
        random_location = (x, y) = game.generate_random_numbers(grid)
        print('DEBUG random_location: {0}'.format(random_location))
        generate_random_location = False
    if random_location == player_location and random_location != previous_player_location:
        neo_pixel.display(grid, GRID_HEIGHT, GRID_WIDTH, LED_COUNT, update_grid)
        random_question, answer_1, answer_2, answer_3, correct_answer_index, correct_answer \
            = game.ask_random_question(questions)
        display.text(TFT, oled, random_question, 5)
        display.texts(TFT, oled, answer_1, answer_2, answer_3, None, 5)
        response = None
        while True:
            if not btn_1.value():
                response = 1
                break
            if not btn_2.value():
                response = 2
                break
            if not btn_3.value():
                response = 3
                break
        if response == correct_answer_index + 1:
            start_new_thread(music.play, (pwm, music.notes['A4'], music.quarter_note))
            display.text(TFT, oled, game.correct_answer_response(), 5, True, True)
            inventory = player.get_inventory(file_manager)
            player.inventory.append(inventory)
            if 'Red Key' in player.inventory:
                final_question = True
            if 'Red Key' not in player.inventory and not final_question:
                receive_red_key = game.generate_random_number(grid)
                if receive_red_key > 3:
                    start_new_thread(music.play, (pwm, music.notes['E5'], music.quarter_note))
                    display.text(TFT, oled, player.pick_up_red_key(file_manager), 5, True, True)
                    final_question = True
                else:
                    start_new_thread(music.play, (pwm, music.notes['G3'], music.quarter_note))
                    display.text(TFT, oled, player.without_red_key(), 5, True, True)
            elif final_question:
                start_new_thread(music.play, (pwm, music.notes['G5'], music.quarter_note))
                display.text(TFT, oled, game.win(file_manager), 0)
                neo_pixel.win_animation()
                neo_pixel.clear_pixels()
                break
        else:
            start_new_thread(music.play, (pwm, music.notes['G3'], music.quarter_note))
            display.text(TFT, oled, game.incorrect_answer_response(correct_answer), 5, True, True)
        generate_random_location = True
        neo_pixel.display(grid, GRID_HEIGHT, GRID_WIDTH, LED_COUNT, update_grid)
