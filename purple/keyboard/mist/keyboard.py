import board
from digitalio import DigitalInOut

from purple.key import Key

# Keys
#
#     0  1  2  3  4
#     5  6  7  8  9
#    10 11 12 13 14
# 15 16          17 18

class Keyboard:
    name = "Mist"
    keys = [
        Key(DigitalInOut(board.A0)),
        Key(DigitalInOut(board.D25)),
        Key(DigitalInOut(board.MISO)),
        Key(DigitalInOut(board.D4)),
        Key(DigitalInOut(board.D5)),
        Key(DigitalInOut(board.A1)),
        Key(DigitalInOut(board.SCK)),
        Key(DigitalInOut(board.RX)),
        Key(DigitalInOut(board.D13)),
        Key(DigitalInOut(board.D6)),
        Key(DigitalInOut(board.A2)),
        Key(DigitalInOut(board.MOSI)),
        Key(DigitalInOut(board.TX)),
        Key(DigitalInOut(board.D12)),
        Key(DigitalInOut(board.D9)),
        Key(DigitalInOut(board.A3)),
        Key(DigitalInOut(board.D24)),
        Key(DigitalInOut(board.D11)),
        Key(DigitalInOut(board.D10)),
    ]