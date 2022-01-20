import board
from digitalio import DigitalInOut

from purple.key import Key

# Keys
#
#  0  1  2  3  4
#  5  6  7  8  9
# 10 11 12 13 14
#            15 16

class Keyboard:
    name = "Ferris Sweep (Left)"
    keys = [
        Key(DigitalInOut(board.D7)),  # 0
        Key(DigitalInOut(board.A0)),  # 1
        Key(DigitalInOut(board.A1)),  # 2
        Key(DigitalInOut(board.A2)),  # 3
        Key(DigitalInOut(board.A3)),  # 4
        Key(DigitalInOut(board.SCK)),  # 5
        Key(DigitalInOut(board.MISO)),  # 6
        Key(DigitalInOut(board.MOSI)),  # 7
        Key(DigitalInOut(board.D10)),  # 8
        Key(DigitalInOut(board.D0)),  # 9
        Key(DigitalInOut(board.D2)),  # 10
        Key(DigitalInOut(board.D3)),  # 11
        Key(DigitalInOut(board.D4)),  # 12
        Key(DigitalInOut(board.D5)),  # 13
        Key(DigitalInOut(board.D6)),  # 14
        Key(DigitalInOut(board.D8)),  # 15
        Key(DigitalInOut(board.D9)),  # 16
    ]