import supervisor
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse

from purple.status import Status


class Core:
    _HOLD_DELAY = 200
    _MOUSE_REPEAT_RATE = 20

    def __init__(self, keys, layout, *extras):
        self._keys = keys
        self._layout = layout
        self._extras = extras
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
        self._current_time = supervisor.ticks_ms()
        self._prior_time = self._current_time
        self._prior_mouse_time = self._current_time
        self._prior_change_time = self._current_time

    def _add_to_buffer(self, keycodes):
        for keycode in keycodes:
            if keycode not in self._key_buffer:
                self._key_buffer.append(keycode)

    def _calc_chord(self):
        val = 0
        for i in range(len(self._keys)):
            key = self._keys[i]
            if key.current or key.just_released:
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
    
    def media_press(self, consumer_control_code, action, hold):
        self._consumer_control.press(consumer_control_code)
        if not (hold and action.hold):
            self._release_all()

    def mouse_move(self, x, y, wheel, action, hold):
        self._mouse.move(x, y, wheel)
        if hold and action.hold:
            self._prior_mouse_time = supervisor.ticks_ms()
            self._held_mouse_movement = (x, y, wheel)
    
    def mouse_press(self, mouse_button, action, hold):
        self._mouse.press(mouse_button)
        if not (hold and action.hold):
            self._release_all()

    def one_shot(self, keycodes):
        for keycode in keycodes:
            if keycode in self._key_buffer:
                self._key_buffer.remove(keycode)
            else:
                self._key_buffer.append(keycode)

    def press(self, keycodes, action, hold):
        # locked keys
        self._add_to_buffer(self._lock_key_buffer)
        # auto mod
        if hold and action.auto_mod:
            self._add_to_buffer(self._layout.auto_mod)
        # primary keys
        self._add_to_buffer(keycodes)
        self._keyboard.press(*self._key_buffer)
        if not (hold and action.hold):
            self._release_all()
        self._key_buffer.clear()

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
                self._prior_time = self._current_time
                self._current_time = supervisor.ticks_ms()

                # If the time value has wrapped, update the prior times.
                if self._current_time < self._prior_time:
                    self._prior_time = self._current_time
                    self._prior_change_time = self._current_time
                    self._prior_mouse_time = self._current_time

                # Keys
                for key in self._keys:
                    key.update()
                    if key.current:
                        down += 1
                    if key.just_pressed:
                        new_down += 1
                    elif key.just_released:
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
                    self._prior_change_time = self._current_time
                elif (
                    down
                    and not self._pressed
                    and (self._current_time - self._prior_change_time) > Core._HOLD_DELAY
                ):
                    self._entering = True
                    self._pressed = True
                    self._press_chord(True)
                
                # Mouse
                if self._held_mouse_movement:
                    while (self._current_time - self._prior_mouse_time) > Core._MOUSE_REPEAT_RATE:
                        self._prior_mouse_time += Core._MOUSE_REPEAT_RATE
                        self._mouse.move(*self._held_mouse_movement)

                # Extras
                if self._extras:
                    status = Status(
                        self._current_time,
                        self._current_time - self._prior_time,
                        self._layout.layers[self.layer_index],
                        tuple(k.current for k in self._keys),
                        self._key_buffer,
                        self._lock_key_buffer
                    )
                    for extra in self._extras:
                        extra.update(status)
        finally:
            self._release_all()
