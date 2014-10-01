from .block import UNKNOWN         # Dummy value for getitem.

def connect(logging=False):
    return World(logging)

class World:

    def __init__(self, logging=False):

        self.logging = logging
        if logging:
            self._log = []


    def __getitem__(self, key):

        value = UNKNOWN         # Dummy value.
        if self.logging:
            self._log.append(('world.getBlock', key, value))
        return value


    def __setitem__(self, key, value):

        if self.logging:
            self._log.append(('world.setBlock', key, value))
