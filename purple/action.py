class Action:
    def __init__(self, tap_action, hold_action=None, hold=False, auto_mod=True):
        self._tap_action = tap_action
        self._hold_action = hold_action
        self.hold = hold
        self.auto_mod = auto_mod

    def run(self, core, hold):
        if hold and self._hold_action is not None:
            self._hold_action.run(core, self, hold)
        else:
            self._tap_action.run(core, self, hold)


class Lock:
    def __init__(self, *keycodes):
        self._keycodes = keycodes

    def run(self, core, action, hold):
        core.toggle_lock(self._keycodes)


class MediaPress:
    def __init__(self, consumer_control_code):
        self._consumer_control_code = consumer_control_code

    def run(self, core, action, hold):
        core.media_press(self._consumer_control_code, action, hold)


class MouseMove:
    def __init__(self, x, y, wheel=0):
        self._x = x
        self._y = y
        self._wheel = wheel

    def run(self, core, action, hold):
        core.mouse_move(self._x, self._y, self._wheel, action, hold)


class MousePress:
    def __init__(self, mouse_button):
        self._mouse_button = mouse_button

    def run(self, core, action, hold):
        core.mouse_press(self._mouse_button, action, hold)


class OneShot:
    def __init__(self, *keycodes):
        self._keycodes = keycodes

    def run(self, core, action, hold):
        core.one_shot(self._keycodes)


class Press:
    def __init__(self, *keycodes):
        self._keycodes = keycodes

    def run(self, core, action, hold):
        core.press(self._keycodes, action, hold)


class ToLayer:
    def __init__(self, index):
        self._index = index

    def run(self, core, action, hold):
        core.layer_index = self._index
