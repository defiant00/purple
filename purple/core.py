import board
import neopixel
import supervisor
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse


class Core:
    _HOLD_DELAY = 200
    _MOUSE_REPEAT_RATE = 20
    _MODIFIER_BLINK = 500
    _MODIFIER_BLINK_ON = 100
    _LOCK_FADE = 800
    _LOCK_FADE_MIN = 0.1
    _LOCK_FADE_NO_COLOR = (32, 32, 32)
    _MOD_COLORS = {
        Keycode.LEFT_SHIFT: (255, 255, 0),
        Keycode.RIGHT_SHIFT: (255, 255, 0),
        Keycode.LEFT_CONTROL: (255, 0, 0),
        Keycode.RIGHT_CONTROL: (255, 0, 0),
        Keycode.LEFT_ALT: (0, 0, 255),
        Keycode.RIGHT_ALT: (0, 0, 255),
        Keycode.LEFT_GUI: (255, 0, 255),
        Keycode.RIGHT_GUI: (255, 0, 255),
    }

    def __init__(self, keys, layout):
        self._keys = keys
        self._layout = layout
        self._led = neopixel.NeoPixel(board.NEOPIXEL, 1)
        self._consumer_control = ConsumerControl(usb_hid.devices)
        self._keyboard = Keyboard(usb_hid.devices)
        self._mouse = Mouse(usb_hid.devices)
        # Whether we're currently entering a chord or releasing one.
        self._entering = True
        # Whether the current chord has been pressed through holding.
        self._pressed = False
        self.layer_index = 0
        self._key_buffer = []
        self._lock_key_buffer = []
        self._held_mouse_movement = ()
        self._prior_mouse_time = supervisor.ticks_ms()
        self._prior_change_time = supervisor.ticks_ms()

    def _add_to_buffer(self, keycodes):
        for keycode in keycodes:
            if keycode not in self._key_buffer:
                self._key_buffer.append(keycode)

    def _calc_chord(self):
        val = 0
        for i in range(len(self._keys)):
            key = self._keys[i]
            if key.current or key.prior:
                val += (1<<i)
        return val

    def _press_chord(self, hold):
        chord = self._calc_chord()
        for i in range(self.layer_index, -1, -1):
            chords = self._layout.layers[i].chords
            if chord in chords:
                chords[chord].run(self, hold)
                return
    
    def _release_all(self):
        self._consumer_control.release()
        self._keyboard.release_all()
        self._mouse.release_all()
        self._held_mouse_movement = ()

    def press(self, keycodes, action, hold):
        if len(keycodes) == 1 and keycodes[0] in Core._MOD_COLORS:
            if keycodes[0] in self._key_buffer:
                self._key_buffer.remove(keycodes[0])
            else:
                self._key_buffer.append(keycodes[0])
        else:
            # locked keys
            self._add_to_buffer(self._lock_key_buffer)
            # auto mod
            if hold and action.auto_mod:
                self._add_to_buffer(self._layout.auto_mod)
            # primary keys
            self._add_to_buffer(keycodes)
            self._keyboard.press(*self._key_buffer)
            if not (hold and action.repeat):
                self._release_all()
            self._key_buffer.clear()
    
    def media_press(self, consumer_control_code, action, hold):
        self._consumer_control.press(consumer_control_code)
        if not (hold and action.repeat):
            self._release_all()
    
    def mouse_press(self, mouse_button, action, hold):
        self._mouse.press(mouse_button)
        if not (hold and action.repeat):
            self._release_all()
    
    def mouse_move(self, x, y, wheel, action, hold):
        self._mouse.move(x, y, wheel)
        if hold and action.repeat:
            self._prior_mouse_time = supervisor.ticks_ms()
            self._held_mouse_movement = (x, y, wheel)
    
    def toggle_lock(self, keycodes):
        for keycode in keycodes:
            if keycode in self._lock_key_buffer:
                self._lock_key_buffer.remove(keycode)
            else:
                self._lock_key_buffer.append(keycode)

    def run(self):
        try:
            while True:
                down = 0
                new_down = 0
                new_up = 0
                current_time = supervisor.ticks_ms()

                # If the time value has wrapped, update the prior time.
                if current_time < self._prior_change_time:
                    self._prior_change_time = current_time
                if current_time < self._prior_mouse_time:
                    self._prior_mouse_time = current_time

                # Keys
                for key in self._keys:
                    key.update()
                    if key.current:
                        down += 1
                    if key.current and not key.prior:
                        new_down += 1
                    elif not key.current and key.prior:
                        new_up += 1

                if new_up and self._entering:
                    # A key has been let up while entering a chord.
                    if not self._pressed:
                        self._press_chord(False)
                    else:
                        self._release_all()
                    self._entering = False
                if new_down:
                    self._entering = True
                    if self._pressed:
                        self._release_all()
                if new_down or new_up:
                    self._pressed = False
                    self._prior_change_time = current_time
                elif (
                    down
                    and not self._pressed
                    and (current_time - self._prior_change_time) > Core._HOLD_DELAY
                ):
                    self._entering = True
                    self._pressed = True
                    self._press_chord(True)
                
                # Mouse
                while (
                    self._held_mouse_movement
                    and (current_time - self._prior_mouse_time) > Core._MOUSE_REPEAT_RATE
                ):
                    self._prior_mouse_time += Core._MOUSE_REPEAT_RATE
                    self._mouse.move(*self._held_mouse_movement)

                # LED Colors
                if (
                    self._key_buffer
                    and (current_time % Core._MODIFIER_BLINK) < Core._MODIFIER_BLINK_ON
                ):
                    index = (
                        current_time % (len(self._key_buffer) * Core._MODIFIER_BLINK)
                    ) // Core._MODIFIER_BLINK
                    color = Core._MOD_COLORS[self._key_buffer[index]]
                else:
                    color = self._layout.layers[self.layer_index].color
                
                lock_mult = 1
                if self._lock_key_buffer:
                    lock_mult = (
                        abs(current_time % (Core._LOCK_FADE * 2) - Core._LOCK_FADE) / Core._LOCK_FADE
                    ) * (1 - Core._LOCK_FADE_MIN) + Core._LOCK_FADE_MIN
                    if color == (0, 0, 0):
                        color = Core._LOCK_FADE_NO_COLOR

                self._led.fill(tuple(lock_mult*i for i in color))
        finally:
            self._release_all()
