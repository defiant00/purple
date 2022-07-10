from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

from purple.action import Action, Lock, MediaPress, MouseMove, MousePress, OneShot, Press, ToLayer
from purple.helpers import key
from purple.layer import Layer

# Keys
#  
#  8  9  10 11 :::: <-- OLED
#  0  1  2  3  ::::
#  4  5  6  7   Q   <-- Encoder
#

class Layout:
    name = "ARTSEY (Left)"
    auto_mod = []
    layers = [
        Layer(
            "Base",
            {
                key(3): Action(Press(Keycode.A), ToLayer(2)),
                key(4) + key(7): Action(Press(Keycode.B)),
                key(6) + key(7): Action(Press(Keycode.C)),
                key(1) + key(2) + key(3): Action(Press(Keycode.D)),
                key(7): Action(Press(Keycode.E), ToLayer(3)),
                key(2) + key(3): Action(Press(Keycode.F)),
                key(1) + key(2): Action(Press(Keycode.G)),
                key(5) + key(7): Action(Press(Keycode.H)),
                key(5): Action(Press(Keycode.I)),
                key(0) + key(1): Action(Press(Keycode.J)),
                key(4) + key(6): Action(Press(Keycode.K)),
                key(5) + key(6) + key(7): Action(Press(Keycode.L)),
                key(4) + key(5) + key(6): Action(Press(Keycode.M)),
                key(4) + key(5): Action(Press(Keycode.N)),
                key(4): Action(Press(Keycode.O), ToLayer(4)),
                key(4) + key(5) + key(7): Action(Press(Keycode.P)),
                key(0) + key(1) + key(3): Action(Press(Keycode.Q)),
                key(2): Action(Press(Keycode.R)),
                key(0): Action(Press(Keycode.S), ToLayer(1)),
                key(1): Action(Press(Keycode.T)),
                key(5) + key(6): Action(Press(Keycode.U)),
                key(0) + key(2): Action(Press(Keycode.V)),
                key(0) + key(3): Action(Press(Keycode.W)),
                key(0) + key(1) + key(2): Action(Press(Keycode.X)),
                key(6): Action(Press(Keycode.Y)),
                key(0) + key(1) + key(2) + key(3): Action(Press(Keycode.Z)),

                key(2) + key(3) + key(4): Action(Press(Keycode.ESCAPE)),
                key(3) + key(7): Action(Press(Keycode.ENTER)),
                key(1) + key(2) + key(3) + key(4): Action(Press(Keycode.TAB)),
                key(3) + key(5) + key(6): Action(Press(Keycode.QUOTE)),
                key(0) + key(7): Action(OneShot(Keycode.CONTROL), Press(Keycode.CONTROL, False), hold=True),
                key(3) + key(6): Action(Press(Keycode.PERIOD)),
                key(0) + key(6): Action(OneShot(Keycode.GUI)),
                key(3) + key(5): Action(Press(Keycode.COMMA)),
                key(0) + key(5): Action(OneShot(Keycode.ALT)),
                key(3) + key(4): Action(Press(Keycode.FORWARD_SLASH)),
                key(0) + key(1) + key(2) + key(7): Action(OneShot(Keycode.SHIFT), Press(Keycode.SHIFT, False), hold=True),
                key(1) + key(5): Action(Press(Keycode.SHIFT, Keycode.ONE)), #Exclamation
                key(2) + key(6): Action(Lock(Keycode.SHIFT)),
                key(4) + key(5) + key(6) + key(7): Action(Press(Keycode.SPACE)),
                key(3) + key(4) + key(5) + key(6): Action(Press(Keycode.CAPS_LOCK)),
                key(2) + key(7): Action(Press(Keycode.BACKSPACE), hold=True),
                key(2) + key(5): Action(Press(Keycode.DELETE)),

                key(2) + key(5) + key(7): Action(ToLayer(5)),
                key(1) + key(3) + key(6): Action(ToLayer(6)),
            },
            (0, 0, 0)
        ),
        Layer(
            "Numbers",
            {
                key(0): Action(ToLayer(0)),
                key(3): Action(Press(Keycode.ONE)),
                key(2): Action(Press(Keycode.TWO)),
                key(1): Action(Press(Keycode.THREE)),
                key(7): Action(Press(Keycode.FOUR)),
                key(6): Action(Press(Keycode.FIVE)),
                key(5): Action(Press(Keycode.SIX)),
                key(2) + key(3): Action(Press(Keycode.SEVEN)),
                key(1) + key(2): Action(Press(Keycode.EIGHT)),
                key(6) + key(7): Action(Press(Keycode.NINE)),
                key(5) + key(6): Action(Press(Keycode.ZERO)),
            },
            (0, 64, 64)
        ),
        Layer(
            "Brackets",
            {
                key(3): Action(ToLayer(0)),
                key(0): Action(Press(Keycode.SHIFT, Keycode.RIGHT_BRACKET)),
                key(1): Action(Press(Keycode.SHIFT, Keycode.NINE)),
                key(2): Action(Press(Keycode.SHIFT, Keycode.ZERO)),
                key(4): Action(Press(Keycode.SHIFT, Keycode.LEFT_BRACKET)),
                key(5): Action(Press(Keycode.LEFT_BRACKET)),
                key(6): Action(Press(Keycode.RIGHT_BRACKET)),
            },
            (0, 0, 64)
        ),
        Layer(
            "Symbols",
            {
                key(0): Action(Press(Keycode.GRAVE_ACCENT)),
                key(1): Action(Press(Keycode.SEMICOLON)),
                key(2): Action(Press(Keycode.BACKSLASH)),
                key(3): Action(Press(Keycode.SHIFT, Keycode.ONE)),
                key(4): Action(Press(Keycode.EQUALS)),
                key(5): Action(Press(Keycode.MINUS)),
                key(6): Action(Press(Keycode.SHIFT, Keycode.FORWARD_SLASH)),
                key(7): Action(ToLayer(0)),
            },
            (64, 0, 64)
        ),
        Layer(
            "Extras",
            {
                key(1): Action(MediaPress(ConsumerControlCode.VOLUME_INCREMENT), hold=True),
                key(2): Action(Press(Keycode.INSERT)),
                key(3): Action(MediaPress(ConsumerControlCode.MUTE)),
                key(4): Action(ToLayer(0)),
                key(5): Action(MediaPress(ConsumerControlCode.VOLUME_DECREMENT), hold=True),
                key(6): Action(Press(Keycode.PRINT_SCREEN)),
                key(7): Action(Press(Keycode.RIGHT_SHIFT)),
            },
            (64, 0, 0)
        ),
        Layer(
            "Navigation",
            {
                key(0): Action(Press(Keycode.PAGE_UP)),
                key(1): Action(Press(Keycode.HOME)),
                key(2): Action(Press(Keycode.UP_ARROW), hold=True),
                key(3): Action(Press(Keycode.END)),
                key(4): Action(Press(Keycode.PAGE_DOWN)),
                key(5): Action(Press(Keycode.LEFT_ARROW), hold=True),
                key(6): Action(Press(Keycode.DOWN_ARROW), hold=True),
                key(7): Action(Press(Keycode.RIGHT_ARROW), hold=True),

                key(2) + key(5) + key(7): Action(ToLayer(0)),
            },
            (64, 64, 0)
        ),
        Layer(
            "Mouse",
            {
                key(0): Action(MouseMove(0, 0, 1), hold=True),
                key(1): Action(MousePress(Mouse.RIGHT_BUTTON)),
                key(2): Action(MouseMove(0, -8), hold=True),
                key(3): Action(MousePress(Mouse.LEFT_BUTTON)),
                key(4): Action(MouseMove(0, 0, -1), hold=True),
                key(5): Action(MouseMove(-8, 0), hold=True),
                key(6): Action(MouseMove(0, 8), hold=True),
                key(7): Action(MouseMove(8, 0), hold=True),

                key(1) + key(3) + key(6): Action(ToLayer(0)),
            },
            (0, 64, 0)
        ),
    ]
