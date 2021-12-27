from adafruit_hid.keycode import Keycode

from purple.action import Action, Press, ToLayer
from purple.layer import Layer


class Layout:
    auto_mod = [Keycode.SHIFT]
    layers = [
        Layer(
            {
                0b00000000000000001: Action(Press(Keycode.Q)),
                0b00000000000000010: Action(Press(Keycode.W)),
                0b00000000000000100: Action(Press(Keycode.F)),
                0b00000000000001000: Action(Press(Keycode.P)),
                0b00000000000010000: Action(Press(Keycode.B)),

                0b00000000000011000: Action(ToLayer(1)),

                0b00000000000100000: Action(Press(Keycode.A)),
                0b00000000001000000: Action(Press(Keycode.R)),
                0b00000000010000000: Action(Press(Keycode.S)),
                0b00000000100000000: Action(Press(Keycode.T)),
                0b00000001000000000: Action(Press(Keycode.G)),

                0b00000000001100000: Action(Press(Keycode.O)),
                0b00000000110000000: Action(Press(Keycode.BACKSPACE), repeat=True),

                0b00000010000000000: Action(Press(Keycode.Z), Press(Keycode.CONTROL, Keycode.Z)),
                0b00000100000000000: Action(Press(Keycode.X)),
                0b00001000000000000: Action(Press(Keycode.C)),
                0b00010000000000000: Action(Press(Keycode.D)),
                0b00100000000000000: Action(Press(Keycode.V)),

                0b01000000000000000: Action(Press(Keycode.TAB)),
                0b10000000000000000: Action(Press(Keycode.SPACE), repeat=True),

                0b00000110000000000: Action(Press(Keycode.SHIFT), Press(Keycode.CAPS_LOCK)),
                0b00001100000000000: Action(Press(Keycode.CONTROL)),
                0b00011000000000000: Action(Press(Keycode.GUI)),
                0b00110000000000000: Action(Press(Keycode.ALT)),
            },
            (0, 0, 0)
        ),
        Layer(
            {
                0b00000000000000001: Action(ToLayer(0)),
                0b00000000000000010: Action(Press(Keycode.SEVEN)),
                0b00000000000000100: Action(Press(Keycode.EIGHT)),
                0b00000000000001000: Action(Press(Keycode.NINE)),

                0b00000000000011000: Action(ToLayer(0)),

                0b00000000001000000: Action(Press(Keycode.FOUR)),
                0b00000000010000000: Action(Press(Keycode.FIVE)),
                0b00000000100000000: Action(Press(Keycode.SIX)),

                0b00000010000000000: Action(Press(Keycode.ZERO)),
                0b00000100000000000: Action(Press(Keycode.ONE)),
                0b00001000000000000: Action(Press(Keycode.TWO)),
                0b00010000000000000: Action(Press(Keycode.THREE)),

                0b01000000000000000: Action(Press(Keycode.PERIOD)),
                0b10000000000000000: Action(Press(Keycode.ENTER)),
            },
            (0, 64, 64)
        ),
    ]
