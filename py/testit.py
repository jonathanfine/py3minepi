'''First steps in using the API

These are MY first steps, and so a bit wobbly.  It is not recommended
practice for new Minecraft progammers.

It puts up four blocks of dirt next to the player, and then replaces
them by air.
'''

# Imports need to built a world by hand.
from minecraft.lowlevel import LowLevelInterface
from minecraft.lowlevel import Connection
from minecraft.world import world_factory

if 1:

    ## Imports needed for the demo.
    from time import sleep
    import sys
    import os

    ## Find address on command line, environment or default.
    if len(sys.argv) == 2:
        address = sys.argv[1]
    else:
        address = os.environ.get('RASPBERRYPI')
        if not address:
            address = 'localhost'

    ## Here's how to connect to a Minecraft game, by hand.
    c = Connection(address, 4711) # Connect.
    lli = LowLevelInterface(c)    # Create a low-level interface.
    world = world_factory(lli)    # Create a World object.

    player = world.player       # The world has a player.

    ## Helper functions.
    def show_player():
        format = 'Player is at: {0}'.format
        print(format(player.pos))

    i_am_here = tuple(map(int, player.pos))

    def vec_add(vec1, vec2):
        return tuple(
            a + b
            for a, b in zip(vec1, vec2)
        )

    ## Get ready for the demo.
    show_player()

    vectors = [
        [1, 0, 1],
        [1, 0, -1],
        [-1, 0, -1],
        [-1, 0, 1],
    ]

    ## Put up some DIRT (code 3).
    for vec in vectors:
        pos = vec_add(i_am_here, vec)
        world[pos] = 3

    sleep(3)

    ## Replace the DIRT by AIR (code 0).
    for vec in vectors:
        pos = vec_add(i_am_here, vec)
        world[pos] = 0
