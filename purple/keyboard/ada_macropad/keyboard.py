import board
from digitalio import DigitalInOut

from purple.key import Key

# Keys
#  
#  8  9  10 11 :::: <-- OLED
#  0  1  2  3  ::::
#  4  5  6  7   Q   <-- Encoder
#

class Keyboard:
    name = "Adafruit Macropad (Left)"
    keys = [
        Key(DigitalInOut(board.KEY11)),  # 4
        Key(DigitalInOut(board.KEY8)),  # 5
        Key(DigitalInOut(board.KEY5)),  # 6
        Key(DigitalInOut(board.KEY2)),  # 7
        Key(DigitalInOut(board.KEY12)),  # 8
        Key(DigitalInOut(board.KEY9)),  # 9
        Key(DigitalInOut(board.KEY6)),  # 10
        Key(DigitalInOut(board.KEY3)),  # 11
        Key(DigitalInOut(board.KEY10)),  # 0
        Key(DigitalInOut(board.KEY7)),  # 1
        Key(DigitalInOut(board.KEY4)),  # 2
        Key(DigitalInOut(board.KEY1)),  # 3
    ]