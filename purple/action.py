class Action:
    def __init__(self, tap, hold=None, repeat=False, auto_mod=True):
        self._tap = tap
        self._hold = hold
        self.repeat = repeat
        self.auto_mod = auto_mod

    def run(self, core, hold):
        if hold and self._hold is not None:
            self._hold.run(core, self, hold)
        else:
            self._tap.run(core, self, hold)


class Lock:
    def __init__(self, *keycodes):
        self._keycodes = keycodes
    
    def run(self, core, action, hold):
        core.toggle_lock(self._keycodes)


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
