![image](https://github.com/mytechnotalent/Pico-Escape-Room/blob/main/MicroPython%20Pico%20Escape%20Room.png?raw=true)

# Pico Escape Room
Raspberry Pi Pico Escape Room game.

## Parts
[Raspberry Pi Pico](https://www.canakit.com/raspberry-pi-pico.html?cid=usd&src=raspberrypi)<br>
[Set of 2 x 20-pin Headers for Raspberry Pi Pico](https://www.canakit.com/set-of-2-20-pin-headers-for-raspberry-pi-pico.html)<br>
[4PCS Breadboards Kit Include 2PCS 830 Point 2PCS 400 Point Solderless](https://www.amazon.com/Breadboards-Solderless-Breadboard-Distribution-Connecting/dp/B07DL13RZH)<br>
[Jumper Wires Male to Male - Pack of 30](https://www.canakit.com/jumper-wires-male-to-male-6.html)<br>
[20 Pcs 6 mm 2 Pin Momentary Tactile Tact Push Button Switch Through Hole Breadboard](https://www.amazon.com/Momentary-Tactile-Through-Breadboard-Friendly/dp/B07WF76VHT)<br>
[9mmx5.5mm Electronic Alarm PCB Panel Mounting Piezo Passive Buzzer Sounder (Pack of 10)](https://www.amazon.com/a15091400ux0103-Electronic-Mounting-Passive-Sounder/dp/B018I1WBNQ)<br>
[8X8 LED Matrix WS2812 5050 SMD RGB LEDs 64 Pixels LED Matrix](https://www.amazon.com/DIYmall-Matrix-WS2812-Inserted-Arduino/dp/B07T2D4QGJ)<br>
[1.44" Colorful SPI TFT LCD Display ST7735 128X128](https://www.amazon.com/HiLetgo-Colorful-Display-128X128-Replace/dp/B073R6SQRY)<br>
[Micro USB Cable High Speed Data and Charging, Nylon Braided Charger Cord, 3-Pack, 3 Feet](https://www.amazon.com/Rankie-Micro-Charging-Braided-3-Pack/dp/B01JPDTZXK)<br>

## Schematic
![image](https://github.com/mytechnotalent/Pico-Escape-Room/blob/main/schematic.png?raw=true)

## Copy Files To Pico, Install Pico-Go
```bash
https://marketplace.visualstudio.com/items?itemName=ChrisWood.pico-go
```

## Run Tests
```bash
import unittest
unittest.main('test_file_manager')
unittest.main('test_game')
unittest.main('test_grid')
unittest.main('test_player')
unittest.main('test_escape_room_player')
```

## License
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)
