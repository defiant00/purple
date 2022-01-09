from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

from purple.action import Action, Lock, MouseMove, MousePress, OneShot, Press, ToLayer
from purple.layer import Layer


class Layout:
    auto_mod = []
    layers = [
        Layer(  # Base
            {
                # Base
                0b00000000000100000: Action(Press(Keycode.A)),
                0b00000000000010000: Action(Press(Keycode.B)),
                0b00001000000000000: Action(Press(Keycode.C)),
                0b00000000010100000: Action(Press(Keycode.D)),
                0b00000000010000000: Action(Press(Keycode.E)),
                0b00000000000000100: Action(Press(Keycode.F)),
                0b00000010000000000: Action(Press(Keycode.G)),
                0b00000000101000000: Action(Press(Keycode.H)),
                0b00000000011000000: Action(Press(Keycode.I)),
                0b00001110000000000: Action(Press(Keycode.J)),
                0b00000000000000110: Action(Press(Keycode.K)),
                0b00000000011100000: Action(Press(Keycode.L)),
                0b00000001000000000: Action(Press(Keycode.M)),
                0b00000000110000000: Action(Press(Keycode.N)),
                0b00000000001000000: Action(Press(Keycode.O)),
                0b00000000000001000: Action(Press(Keycode.P)),
                0b00000000000000001: Action(Press(Keycode.Q)),
                0b00000000111000000: Action(Press(Keycode.R)),
                0b00000000001100000: Action(Press(Keycode.S)),
                0b00000000100000000: Action(Press(Keycode.T)),
                0b00010000000000000: Action(Press(Keycode.U)),
                0b00100000000000000: Action(Press(Keycode.V)),
                0b00000000000000010: Action(Press(Keycode.W)),
                0b00011100000000000: Action(Press(Keycode.X)),
                0b00000100000000000: Action(Press(Keycode.Y)),
                0b00000110000000000: Action(Press(Keycode.Z)),

                0b00000000000000111: Action(Press(Keycode.GRAVE_ACCENT)),
                0b00000010100000000: Action(Press(Keycode.SEMICOLON)),
                0b00001100000000000: Action(Press(Keycode.PERIOD)),
                0b00011000000000000: Action(Press(Keycode.COMMA)),
                0b00000000100000010: Action(Press(Keycode.LEFT_BRACKET)),
                0b00000000100000100: Action(Press(Keycode.RIGHT_BRACKET)),
                0b00010000100000000: Action(Press(Keycode.QUOTE)),
                0b00000000100001000: Action(Press(Keycode.MINUS)),
                0b00000000010000100: Action(Press(Keycode.EQUALS)),
                0b00100001000000000: Action(Press(Keycode.FORWARD_SLASH)),
                0b00000001000010000: Action(Press(Keycode.BACKSLASH)),

                # Shifted
                0b10000000000100000: Action(Press(Keycode.SHIFT, Keycode.A)),
                0b10000000000010000: Action(Press(Keycode.SHIFT, Keycode.B)),
                0b10001000000000000: Action(Press(Keycode.SHIFT, Keycode.C)),
                0b10000000010100000: Action(Press(Keycode.SHIFT, Keycode.D)),
                0b10000000010000000: Action(Press(Keycode.SHIFT, Keycode.E)),
                0b10000000000000100: Action(Press(Keycode.SHIFT, Keycode.F)),
                0b10000010000000000: Action(Press(Keycode.SHIFT, Keycode.G)),
                0b10000000101000000: Action(Press(Keycode.SHIFT, Keycode.H)),
                0b10000000011000000: Action(Press(Keycode.SHIFT, Keycode.I)),
                0b10001110000000000: Action(Press(Keycode.SHIFT, Keycode.J)),
                0b10000000000000110: Action(Press(Keycode.SHIFT, Keycode.K)),
                0b10000000011100000: Action(Press(Keycode.SHIFT, Keycode.L)),
                0b10000001000000000: Action(Press(Keycode.SHIFT, Keycode.M)),
                0b10000000110000000: Action(Press(Keycode.SHIFT, Keycode.N)),
                0b10000000001000000: Action(Press(Keycode.SHIFT, Keycode.O)),
                0b10000000000001000: Action(Press(Keycode.SHIFT, Keycode.P)),
                0b10000000000000001: Action(Press(Keycode.SHIFT, Keycode.Q)),
                0b10000000111000000: Action(Press(Keycode.SHIFT, Keycode.R)),
                0b10000000001100000: Action(Press(Keycode.SHIFT, Keycode.S)),
                0b10000000100000000: Action(Press(Keycode.SHIFT, Keycode.T)),
                0b10010000000000000: Action(Press(Keycode.SHIFT, Keycode.U)),
                0b10100000000000000: Action(Press(Keycode.SHIFT, Keycode.V)),
                0b10000000000000010: Action(Press(Keycode.SHIFT, Keycode.W)),
                0b10011100000000000: Action(Press(Keycode.SHIFT, Keycode.X)),
                0b10000100000000000: Action(Press(Keycode.SHIFT, Keycode.Y)),
                0b10000110000000000: Action(Press(Keycode.SHIFT, Keycode.Z)),

                0b10000000000000111: Action(Press(Keycode.SHIFT, Keycode.GRAVE_ACCENT)),
                0b10000010100000000: Action(Press(Keycode.SHIFT, Keycode.SEMICOLON)),
                0b10001100000000000: Action(Press(Keycode.SHIFT, Keycode.PERIOD)),
                0b10011000000000000: Action(Press(Keycode.SHIFT, Keycode.COMMA)),
                0b10000000100000010: Action(Press(Keycode.SHIFT, Keycode.LEFT_BRACKET)),
                0b10000000100000100: Action(Press(Keycode.SHIFT, Keycode.RIGHT_BRACKET)),
                0b10010000100000000: Action(Press(Keycode.SHIFT, Keycode.QUOTE)),
                0b10000000100001000: Action(Press(Keycode.SHIFT, Keycode.MINUS)),
                0b10000000010000100: Action(Press(Keycode.SHIFT, Keycode.EQUALS)),
                0b10100001000000000: Action(Press(Keycode.SHIFT, Keycode.FORWARD_SLASH)),
                0b10000001000010000: Action(Press(Keycode.SHIFT, Keycode.BACKSLASH)),

                # Modifiers
                0b00000000100100000: Action(OneShot(Keycode.CONTROL), Press(Keycode.CONTROL), hold=True),
                0b00010000000100000: Action(OneShot(Keycode.ALT), Press(Keycode.ALT), hold=True),
                0b00000001000100000: Action(OneShot(Keycode.GUI), Press(Keycode.GUI), hold=True),

                # Shifted Modifiers
                0b10000000100100000: Action(OneShot(Keycode.SHIFT, Keycode.CONTROL), Press(Keycode.SHIFT, Keycode.CONTROL), hold=True),
                0b10010000000100000: Action(OneShot(Keycode.SHIFT, Keycode.ALT), Press(Keycode.SHIFT, Keycode.ALT), hold=True),
                0b10000001000100000: Action(OneShot(Keycode.SHIFT, Keycode.GUI), Press(Keycode.SHIFT, Keycode.GUI), hold=True),

                # Locked Modifiers
                0b11000000000000000: Action(Lock(Keycode.SHIFT)),
                0b01000000100100000: Action(Lock(Keycode.CONTROL)),
                0b01010000000100000: Action(Lock(Keycode.ALT)),
                0b01000001000100000: Action(Lock(Keycode.GUI)),

                # Other
                0b10000000000000000: Action(Press(Keycode.SPACE), Press(Keycode.SHIFT), hold=True),
                0b00010010000000000: Action(Press(Keycode.TAB)),
                0b00000000111100000: Action(Press(Keycode.ENTER)),
                0b01000000000000000: Action(Press(Keycode.BACKSPACE), hold=True),
                0b00011110000000000: Action(Press(Keycode.DELETE), hold=True),
                0b00000000000000011: Action(Press(Keycode.ESCAPE)),

                0b01000000010000000: Action(ToLayer(1)),
                0b01000000001000000: Action(ToLayer(2)),
                0b01000000100000000: Action(ToLayer(3)),
                0b01000000000100000: Action(ToLayer(4)),
            },
            (0, 0, 0)
        ),
        Layer(  # Nav
            {
                # Base
                0b00000000000000001: Action(Press(Keycode.PAGE_UP)),
                0b00000000000000010: Action(Press(Keycode.HOME)),
                0b00000000000000100: Action(Press(Keycode.UP_ARROW), hold=True),
                0b00000000000001000: Action(Press(Keycode.END)),
                0b00000000000100000: Action(Press(Keycode.PAGE_DOWN)),
                0b00000000001000000: Action(Press(Keycode.LEFT_ARROW), hold=True),
                0b00000000010000000: Action(Press(Keycode.DOWN_ARROW), hold=True),
                0b00000000100000000: Action(Press(Keycode.RIGHT_ARROW), hold=True),

                # Shifted
                0b10000000000000001: Action(Press(Keycode.SHIFT, Keycode.PAGE_UP)),
                0b10000000000000010: Action(Press(Keycode.SHIFT, Keycode.HOME)),
                0b10000000000000100: Action(Press(Keycode.SHIFT, Keycode.UP_ARROW), hold=True),
                0b10000000000001000: Action(Press(Keycode.SHIFT, Keycode.END)),
                0b10000000000100000: Action(Press(Keycode.SHIFT, Keycode.PAGE_DOWN)),
                0b10000000001000000: Action(Press(Keycode.SHIFT, Keycode.LEFT_ARROW), hold=True),
                0b10000000010000000: Action(Press(Keycode.SHIFT, Keycode.DOWN_ARROW), hold=True),
                0b10000000100000000: Action(Press(Keycode.SHIFT, Keycode.RIGHT_ARROW), hold=True),

                # Other
                0b00000001000000000: Action(ToLayer(0)),
            },
            (64, 0, 64)
        ),
        Layer(  # Mouse
            {
                0b00000000000000001: Action(MouseMove(0, 0, 1), hold=True),
                0b00000000000000010: Action(MousePress(Mouse.RIGHT_BUTTON)),
                0b00000000000000100: Action(MouseMove(0, -8), hold=True),
                0b00000000000001000: Action(MousePress(Mouse.LEFT_BUTTON)),
                0b00000000000100000: Action(MouseMove(0, 0, -1), hold=True),
                0b00000000001000000: Action(MouseMove(-8, 0), hold=True),
                0b00000000010000000: Action(MouseMove(0, 8), hold=True),
                0b00000000100000000: Action(MouseMove(8, 0), hold=True),

                0b00000000001000100: Action(MouseMove(-8, -8), hold=True),
                0b00000000100000100: Action(MouseMove(8, -8), hold=True),
                0b00000000110000000: Action(MouseMove(8, 8), hold=True),
                0b00000000011000000: Action(MouseMove(-8, 8), hold=True),

                0b00000001000000000: Action(ToLayer(0)),
            },
            (64, 0, 0)
        ),
        Layer(  # Numbers
            {
                # Base
                0b00000010000000000: Action(Press(Keycode.ZERO)),
                0b00000100000000000: Action(Press(Keycode.ONE)),
                0b00001000000000000: Action(Press(Keycode.TWO)),
                0b00010000000000000: Action(Press(Keycode.THREE)),
                0b00000000001000000: Action(Press(Keycode.FOUR)),
                0b00000000010000000: Action(Press(Keycode.FIVE)),
                0b00000000100000000: Action(Press(Keycode.SIX)),
                0b00000000000000010: Action(Press(Keycode.SEVEN)),
                0b00000000000000100: Action(Press(Keycode.EIGHT)),
                0b00000000000001000: Action(Press(Keycode.NINE)),

                # Shifted
                0b10000010000000000: Action(Press(Keycode.SHIFT, Keycode.ZERO)),
                0b10000100000000000: Action(Press(Keycode.SHIFT, Keycode.ONE)),
                0b10001000000000000: Action(Press(Keycode.SHIFT, Keycode.TWO)),
                0b10010000000000000: Action(Press(Keycode.SHIFT, Keycode.THREE)),
                0b10000000001000000: Action(Press(Keycode.SHIFT, Keycode.FOUR)),
                0b10000000010000000: Action(Press(Keycode.SHIFT, Keycode.FIVE)),
                0b10000000100000000: Action(Press(Keycode.SHIFT, Keycode.SIX)),
                0b10000000000000010: Action(Press(Keycode.SHIFT, Keycode.SEVEN)),
                0b10000000000000100: Action(Press(Keycode.SHIFT, Keycode.EIGHT)),
                0b10000000000001000: Action(Press(Keycode.SHIFT, Keycode.NINE)),

                # Other
                0b00000001000000000: Action(ToLayer(0)),
            },
            (0, 64, 64)
        ),
        Layer(  # Functions
            {
                # Base
                0b00000010000000000: Action(Press(Keycode.F1)),
                0b00000100000000000: Action(Press(Keycode.F2)),
                0b00001000000000000: Action(Press(Keycode.F3)),
                0b00010000000000000: Action(Press(Keycode.F4)),
                0b00000000000100000: Action(Press(Keycode.F5)),
                0b00000000001000000: Action(Press(Keycode.F6)),
                0b00000000010000000: Action(Press(Keycode.F7)),
                0b00000000100000000: Action(Press(Keycode.F8)),
                0b00000000000000001: Action(Press(Keycode.F9)),
                0b00000000000000010: Action(Press(Keycode.F10)),
                0b00000000000000100: Action(Press(Keycode.F11)),
                0b00000000000001000: Action(Press(Keycode.F12)),

                # Shifted
                0b10000010000000000: Action(Press(Keycode.SHIFT, Keycode.F1)),
                0b10000100000000000: Action(Press(Keycode.SHIFT, Keycode.F2)),
                0b10001000000000000: Action(Press(Keycode.SHIFT, Keycode.F3)),
                0b10010000000000000: Action(Press(Keycode.SHIFT, Keycode.F4)),
                0b10000000000100000: Action(Press(Keycode.SHIFT, Keycode.F5)),
                0b10000000001000000: Action(Press(Keycode.SHIFT, Keycode.F6)),
                0b10000000010000000: Action(Press(Keycode.SHIFT, Keycode.F7)),
                0b10000000100000000: Action(Press(Keycode.SHIFT, Keycode.F8)),
                0b10000000000000001: Action(Press(Keycode.SHIFT, Keycode.F9)),
                0b10000000000000010: Action(Press(Keycode.SHIFT, Keycode.F10)),
                0b10000000000000100: Action(Press(Keycode.SHIFT, Keycode.F11)),
                0b10000000000001000: Action(Press(Keycode.SHIFT, Keycode.F12)),

                # Other
                0b00000001000000000: Action(ToLayer(0)),
            },
            (0, 64, 0)
        ),
    ]
