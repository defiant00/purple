from adafruit_hid.keycode import Keycode

from purple.action import Action, Press, ToLayer
from purple.layer import Layer


class Layout:
    auto_mod = []
    layers = [
        Layer(
            {
                0b00000000100000000: Action(Press(Keycode.A), ToLayer(2)),
                0b00000000001001000: Action(Press(Keycode.B)),
                0b00000000000011000: Action(Press(Keycode.C)),
                0b00000011100000000: Action(Press(Keycode.D)),
                0b00000000000001000: Action(Press(Keycode.E), ToLayer(3)),
                0b00000001100000000: Action(Press(Keycode.F)),
                0b00000011000000000: Action(Press(Keycode.G)),
                0b00000000000101000: Action(Press(Keycode.H)),
                0b00000000000100000: Action(Press(Keycode.I)),
                0b00000110000000000: Action(Press(Keycode.J)),
                0b00000000001010000: Action(Press(Keycode.K)),
                0b00000000000111000: Action(Press(Keycode.L)),
                0b00000000001110000: Action(Press(Keycode.M)),
                0b00000000001100000: Action(Press(Keycode.N)),
                0b00000000001000000: Action(Press(Keycode.O)),
                0b00000000001101000: Action(Press(Keycode.P)),
                0b00000110100000000: Action(Press(Keycode.Q)),
                0b00000001000000000: Action(Press(Keycode.R)),
                0b00000100000000000: Action(Press(Keycode.S), ToLayer(1)),
                0b00000010000000000: Action(Press(Keycode.T)),
                0b00000000000110000: Action(Press(Keycode.U)),
                0b00000101000000000: Action(Press(Keycode.V)),
                0b00000100100000000: Action(Press(Keycode.W)),
                0b00000111000000000: Action(Press(Keycode.X)),
                0b00000000000010000: Action(Press(Keycode.Y)),
                0b00000111100000000: Action(Press(Keycode.Z)),

                0b00000001101000000: Action(Press(Keycode.ESCAPE)),
                0b00000000100001000: Action(Press(Keycode.ENTER)),
                0b00000011101000000: Action(Press(Keycode.TAB)),
                0b00000000100110000: Action(Press(Keycode.QUOTE)),
                0b00000100000001000: Action(Press(Keycode.CONTROL)),
                0b00000000100010000: Action(Press(Keycode.PERIOD)),
                0b00000100000010000: Action(Press(Keycode.GUI)),
                0b00000000100100000: Action(Press(Keycode.COMMA)),
                0b00000100000100000: Action(Press(Keycode.ALT)),
                0b00000000101000000: Action(Press(Keycode.FORWARD_SLASH)),
                0b00000111000001000: Action(Press(Keycode.SHIFT)),
                0b00000010000100000: Action(Press(Keycode.SHIFT, Keycode.ONE)),
                # shift lock
                0b00000000001111000: Action(Press(Keycode.SPACE)),
                0b00000000101110000: Action(Press(Keycode.CAPS_LOCK)),
                0b00000001000001000: Action(Press(Keycode.BACKSPACE)),
                0b00000001000100000: Action(Press(Keycode.DELETE)),

                0b00000001000101000: Action(ToLayer(4)),
            },
            (0, 0, 0)
        ),
        Layer(
            {
                0b00000100000000000: Action(ToLayer(0)),
                0b00000000100000000: Action(Press(Keycode.ONE)),
                0b00000001000000000: Action(Press(Keycode.TWO)),
                0b00000010000000000: Action(Press(Keycode.THREE)),
                0b00000000000001000: Action(Press(Keycode.FOUR)),
                0b00000000000010000: Action(Press(Keycode.FIVE)),
                0b00000000000100000: Action(Press(Keycode.SIX)),
                0b00000001100000000: Action(Press(Keycode.SEVEN)),
                0b00000011000000000: Action(Press(Keycode.EIGHT)),
                0b00000000000011000: Action(Press(Keycode.NINE)),
                0b00000000000110000: Action(Press(Keycode.ZERO)),
            },
            (0, 64, 64)
        ),
        Layer(
            {
                0b00000000100000000: Action(ToLayer(0)),
                0b00000100000000000: Action(Press(Keycode.SHIFT, Keycode.RIGHT_BRACKET)),
                0b00000010000000000: Action(Press(Keycode.SHIFT, Keycode.NINE)),
                0b00000001000000000: Action(Press(Keycode.SHIFT, Keycode.ZERO)),
                0b00000000001000000: Action(Press(Keycode.SHIFT, Keycode.LEFT_BRACKET)),
                0b00000000000100000: Action(Press(Keycode.LEFT_BRACKET)),
                0b00000000000010000: Action(Press(Keycode.RIGHT_BRACKET)),
            },
            (0, 0, 64)
        ),
        Layer(
            {
                0b00000100000000000: Action(Press(Keycode.GRAVE_ACCENT)),
                0b00000010000000000: Action(Press(Keycode.SEMICOLON)),
                0b00000001000000000: Action(Press(Keycode.BACKSLASH)),
                0b00000000100000000: Action(Press(Keycode.SHIFT, Keycode.ONE)),
                0b00000000001000000: Action(Press(Keycode.EQUALS)),
                0b00000000000100000: Action(Press(Keycode.MINUS)),
                0b00000000000010000: Action(Press(Keycode.SHIFT, Keycode.FORWARD_SLASH)),
                0b00000000000001000: Action(ToLayer(0)),
            },
            (64, 0, 64)
        ),
        Layer(
            {
                0b00000100000000000: Action(Press(Keycode.PAGE_UP)),
                0b00000010000000000: Action(Press(Keycode.HOME)),
                0b00000001000000000: Action(Press(Keycode.UP_ARROW)),
                0b00000000100000000: Action(Press(Keycode.END)),
                0b00000000001000000: Action(Press(Keycode.PAGE_DOWN)),
                0b00000000000100000: Action(Press(Keycode.LEFT_ARROW)),
                0b00000000000010000: Action(Press(Keycode.DOWN_ARROW)),
                0b00000000000001000: Action(Press(Keycode.RIGHT_ARROW)),

                0b00000001000101000: Action(ToLayer(0)),
            },
            (64, 0, 0)
        ),
    ]
