class Status:
    def __init__(self, time, delta, layer, keys, one_shot_key_buffer, lock_key_buffer):
        self.time = time
        self.delta = delta
        self.layer = layer
        self.keys = keys
        self.one_shot_key_buffer = one_shot_key_buffer
        self.lock_key_buffer = lock_key_buffer