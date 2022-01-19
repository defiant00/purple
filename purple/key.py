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

class MatrixKey:
    def __init__(self, diode_pin, wire_pin):
        self._prior = False
        self.current = False
        self._diode_pin = diode_pin
        self._wire_pin = wire_pin
    
    @property
    def just_pressed(self):
        return self.current and not self._prior
    
    @property
    def just_released(self):
        return self._prior and not self.current

    def update(self):
        self._prior = self.current
        self._wire_pin.value = True
        #self.current = not self._diode_pin.value
        self.current = self._diode_pin.value
        self._wire_pin.value = False
