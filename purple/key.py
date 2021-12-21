from digitalio import Pull
from adafruit_hid.keycode import Keycode


class Key:
    def __init__(self, in_out):
        self.prior = False
        self.current = False
        self._in_out = in_out
        self._in_out.switch_to_input(pull=Pull.UP)

    def update(self):
        self.prior = self.current
        self.current = not self._in_out.value

    def is_mod(keycode):
        return (
            keycode == Keycode.SHIFT
            or keycode == Keycode.CONTROL
            or keycode == Keycode.ALT
            or keycode == Keycode.GUI
        )
