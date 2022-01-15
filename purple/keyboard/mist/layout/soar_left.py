from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

from purple.action import Action, Lock, MouseMove, MousePress, OneShot, Press, ToLayer
from purple.helpers import key
from purple.layer import Layer


class Layout:
    auto_mod = []
    layers = [
        Layer(  # Base
            {
                key(5): Action(Press(Keycode.A)),
                key(10): Action(Press(Keycode.B)),
                key(12): Action(Press(Keycode.C)),
                key(13): Action(Press(Keycode.D)),
                key(7): Action(Press(Keycode.E)),
                key(2): Action(Press(Keycode.F)),
                key(4): Action(Press(Keycode.G)),
                key(6)+key(7): Action(Press(Keycode.H)),
                key(7)+key(8): Action(Press(Keycode.I)),
                key(9)+key(18): Action(Press(Keycode.J)),
                key(1)+key(18): Action(Press(Keycode.K)),
                key(5)+key(18): Action(Press(Keycode.L)),
                key(9): Action(Press(Keycode.M)),
                key(8)+key(18): Action(Press(Keycode.N)),
                key(6): Action(Press(Keycode.O)),
                key(3): Action(Press(Keycode.P)),
                key(14)+key(18): Action(Press(Keycode.Q)),
                key(6)+key(18): Action(Press(Keycode.R)),
                key(7)+key(18): Action(Press(Keycode.S)),
                key(8): Action(Press(Keycode.T)),
                key(11): Action(Press(Keycode.U)),
                key(0): Action(Press(Keycode.V)),
                key(1): Action(Press(Keycode.W)),
                key(11)+key(18): Action(Press(Keycode.X)),
                key(14): Action(Press(Keycode.Y)),
                key(10)+key(18): Action(Press(Keycode.Z)),

                key(4)+key(18): Action(Press(Keycode.GRAVE_ACCENT)),
                key(3)+key(8): Action(Press(Keycode.SEMICOLON)),
                key(11)+key(12): Action(Press(Keycode.PERIOD)),
                key(12)+key(13): Action(Press(Keycode.COMMA)),
                key(2)+key(18): Action(Press(Keycode.LEFT_BRACKET)),
                key(3)+key(18): Action(Press(Keycode.RIGHT_BRACKET)),
                key(8)+key(13): Action(Press(Keycode.QUOTE)),
                key(13)+key(18): Action(Press(Keycode.MINUS)),
                key(12)+key(18): Action(Press(Keycode.EQUALS)),
                key(9)+key(14): Action(Press(Keycode.FORWARD_SLASH)),
                key(4)+key(9): Action(Press(Keycode.BACKSLASH)),
                key(2)+key(7)+key(18): Action(Press(Keycode.SHIFT, Keycode.NINE)),
                key(3)+key(8)+key(18): Action(Press(Keycode.SHIFT, Keycode.ZERO)),

                # Modifiers
                key(5)+key(6): Action(OneShot(Keycode.SHIFT), Press(Keycode.SHIFT), hold=True),
                key(5)+key(8): Action(OneShot(Keycode.CONTROL), Press(Keycode.CONTROL), hold=True),
                key(5)+key(13): Action(OneShot(Keycode.ALT), Press(Keycode.ALT), hold=True),
                key(5)+key(9): Action(OneShot(Keycode.GUI), Press(Keycode.GUI), hold=True),

                # Locked Modifiers
                key(5)+key(6)+key(17): Action(Lock(Keycode.SHIFT)),
                key(17)+key(18): Action(Lock(Keycode.SHIFT)),
                key(5)+key(8)+key(17): Action(Lock(Keycode.CONTROL)),
                key(5)+key(13)+key(17): Action(Lock(Keycode.ALT)),
                key(5)+key(9)+key(17): Action(Lock(Keycode.GUI)),

                # Other
                key(18): Action(Press(Keycode.SPACE), Press(Keycode.SHIFT), hold=True),
                key(5)+key(6)+key(18): Action(Press(Keycode.TAB)),
                key(7)+key(8)+key(18): Action(Press(Keycode.ENTER)),
                key(17): Action(Press(Keycode.BACKSPACE), hold=True),
                key(10)+key(13): Action(Press(Keycode.DELETE), hold=True),
                key(0)+key(18): Action(Press(Keycode.ESCAPE)),

                key(7)+key(17): Action(ToLayer(1)),
                key(6)+key(17): Action(ToLayer(2)),
                key(8)+key(17): Action(ToLayer(3)),
                key(5)+key(17): Action(ToLayer(4)),
            },
            (0, 0, 0)
        ),
        Layer(  # Nav
            {
                key(0): Action(Press(Keycode.PAGE_UP)),
                key(1): Action(Press(Keycode.HOME)),
                key(2): Action(Press(Keycode.UP_ARROW), hold=True),
                key(3): Action(Press(Keycode.END)),
                key(5): Action(Press(Keycode.PAGE_DOWN)),
                key(6): Action(Press(Keycode.LEFT_ARROW), hold=True),
                key(7): Action(Press(Keycode.DOWN_ARROW), hold=True),
                key(8): Action(Press(Keycode.RIGHT_ARROW), hold=True),

                # Shifted
                key(0)+key(18): Action(Press(Keycode.SHIFT, Keycode.PAGE_UP)),
                key(1)+key(18): Action(Press(Keycode.SHIFT, Keycode.HOME)),
                key(2)+key(18): Action(Press(Keycode.SHIFT, Keycode.UP_ARROW), hold=True),
                key(3)+key(18): Action(Press(Keycode.SHIFT, Keycode.END)),
                key(5)+key(18): Action(Press(Keycode.SHIFT, Keycode.PAGE_DOWN)),
                key(6)+key(18): Action(Press(Keycode.SHIFT, Keycode.LEFT_ARROW), hold=True),
                key(7)+key(18): Action(Press(Keycode.SHIFT, Keycode.DOWN_ARROW), hold=True),
                key(8)+key(18): Action(Press(Keycode.SHIFT, Keycode.RIGHT_ARROW), hold=True),

                # Other
                key(9): Action(ToLayer(0)),
            },
            (64, 0, 64)
        ),
        Layer(  # Mouse
            {
                key(0): Action(MouseMove(0, 0, 1), hold=True),
                key(1): Action(MousePress(Mouse.RIGHT_BUTTON)),
                key(2): Action(MouseMove(0, -8), hold=True),
                key(3): Action(MousePress(Mouse.LEFT_BUTTON)),
                key(5): Action(MouseMove(0, 0, -1), hold=True),
                key(6): Action(MouseMove(-8, 0), hold=True),
                key(7): Action(MouseMove(0, 8), hold=True),
                key(8): Action(MouseMove(8, 0), hold=True),

                # Diagonals
                key(2)+key(6): Action(MouseMove(-8, -8), hold=True),
                key(2)+key(8): Action(MouseMove(8, -8), hold=True),
                key(7)+key(8): Action(MouseMove(8, 8), hold=True),
                key(6)+key(7): Action(MouseMove(-8, 8), hold=True),

                # Other
                key(9): Action(ToLayer(0)),
            },
            (64, 0, 0)
        ),
        Layer(  # Numbers
            {
                # Base
                key(5): Action(Press(Keycode.ZERO)),
                key(6): Action(Press(Keycode.ONE)),
                key(7): Action(Press(Keycode.TWO)),
                key(8): Action(Press(Keycode.THREE)),
                key(11): Action(Press(Keycode.FOUR)),
                key(12): Action(Press(Keycode.FIVE)),
                key(13): Action(Press(Keycode.SIX)),
                key(1): Action(Press(Keycode.SEVEN)),
                key(2): Action(Press(Keycode.EIGHT)),
                key(3): Action(Press(Keycode.NINE)),

                # Shifted
                key(5)+key(18): Action(Press(Keycode.SHIFT, Keycode.ZERO)),
                key(6)+key(18): Action(Press(Keycode.SHIFT, Keycode.ONE)),
                key(7)+key(18): Action(Press(Keycode.SHIFT, Keycode.TWO)),
                key(8)+key(18): Action(Press(Keycode.SHIFT, Keycode.THREE)),
                key(11)+key(18): Action(Press(Keycode.SHIFT, Keycode.FOUR)),
                key(12)+key(18): Action(Press(Keycode.SHIFT, Keycode.FIVE)),
                key(13)+key(18): Action(Press(Keycode.SHIFT, Keycode.SIX)),
                key(1)+key(18): Action(Press(Keycode.SHIFT, Keycode.SEVEN)),
                key(2)+key(18): Action(Press(Keycode.SHIFT, Keycode.EIGHT)),
                key(3)+key(18): Action(Press(Keycode.SHIFT, Keycode.NINE)),

                # Other
                key(9): Action(ToLayer(0)),
            },
            (0, 64, 64)
        ),
        Layer(  # Functions
            {
                # Base
                key(10): Action(Press(Keycode.F1)),
                key(11): Action(Press(Keycode.F2)),
                key(12): Action(Press(Keycode.F3)),
                key(13): Action(Press(Keycode.F4)),
                key(5): Action(Press(Keycode.F5)),
                key(6): Action(Press(Keycode.F6)),
                key(7): Action(Press(Keycode.F7)),
                key(8): Action(Press(Keycode.F8)),
                key(0): Action(Press(Keycode.F9)),
                key(1): Action(Press(Keycode.F10)),
                key(2): Action(Press(Keycode.F11)),
                key(3): Action(Press(Keycode.F12)),

                # Shifted
                key(10)+key(18): Action(Press(Keycode.SHIFT, Keycode.F1)),
                key(11)+key(18): Action(Press(Keycode.SHIFT, Keycode.F2)),
                key(12)+key(18): Action(Press(Keycode.SHIFT, Keycode.F3)),
                key(13)+key(18): Action(Press(Keycode.SHIFT, Keycode.F4)),
                key(5)+key(18): Action(Press(Keycode.SHIFT, Keycode.F5)),
                key(6)+key(18): Action(Press(Keycode.SHIFT, Keycode.F6)),
                key(7)+key(18): Action(Press(Keycode.SHIFT, Keycode.F7)),
                key(8)+key(18): Action(Press(Keycode.SHIFT, Keycode.F8)),
                key(0)+key(18): Action(Press(Keycode.SHIFT, Keycode.F9)),
                key(1)+key(18): Action(Press(Keycode.SHIFT, Keycode.F10)),
                key(2)+key(18): Action(Press(Keycode.SHIFT, Keycode.F11)),
                key(3)+key(18): Action(Press(Keycode.SHIFT, Keycode.F12)),

                # Other
                key(9): Action(ToLayer(0)),
            },
            (0, 64, 0)
        ),
    ]
