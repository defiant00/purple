from purple.key import Key


class Action:
    def __init__(self, tap, hold=None, repeat=False, auto_mod=True):
        self.tap = tap
        self.hold = hold
        self.repeat = repeat
        self.auto_mod = auto_mod

    def run(self, core, hold):
        if hold and self.hold is not None:
            self.hold.run(core, self, hold)
        else:
            self.tap.run(core, self, hold)


class Press:
    def __init__(self, *keycodes):
        self.keycodes = keycodes

    def run(self, core, action, hold):
        if len(self.keycodes) == 1 and Key.is_mod(self.keycodes[0]):
            core.toggle_buffer(self.keycodes[0])
        else:
            if hold and action.auto_mod:
                core.add_auto_mod()
            core.add_to_buffer(self.keycodes)
            core.press_buffer()
            if not (hold and action.repeat):
                core.release_all()
            core.clear_buffer()


class ToLayer:
    def __init__(self, index):
        self._index = index

    def run(self, core, action, hold):
        core.layer_index = self._index
