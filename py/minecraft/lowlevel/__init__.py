'''Low-level interface to Minecraft

To use
>>> c = Connection('localhost', 4711)
>>> w = LowLevelInterface(c)
>>> w.player_get_pos()

'''

from .commands import SIGNATURES
from .tools import build_command
from .tools import Connection   # And available for export.


class LowLevelInterface:

    def __init__(self, connection):

        self.send = connection.send
        self.receive = connection.receive
        self.read_error = connection.read_error


# Patch the commands into the low level interface.
for key, value in SIGNATURES.items():

    setattr(LowLevelInterface, key, build_command(*value))
