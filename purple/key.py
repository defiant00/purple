from digitalio import Pull
from adafruit_hid.keycode import Keycode


class Key:
    def __init__(self, pin):
        self._prior = False
        self.current = False
        self._pin = pin
        self._pin.switch_to_input(pull=Pull.UP)
    
    @property
    def just_pressed(self):
        return self.current and not self._prior
    
    @property
    def just_released(self):
        return self._prior and not self.current

    def update(self):
        self._prior = self.current
        self.current = not self._pin.value
