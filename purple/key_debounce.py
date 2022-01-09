from digitalio import Pull
from adafruit_debouncer import Debouncer
from adafruit_hid.keycode import Keycode


class Key:
    def __init__(self, pin):
        pin.switch_to_input(pull=Pull.UP)
        self._switch = Debouncer(pin, interval=0.005)

    @property
    def current(self):
        return not self._switch.value
    
    @property
    def just_pressed(self):
        return self._switch.fell
    
    @property
    def just_released(self):
        return self._switch.rose

    def update(self):
        self._switch.update()
