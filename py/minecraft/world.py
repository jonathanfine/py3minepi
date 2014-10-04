# import .block as block
from .lowlevel import Connection
from .lowlevel import LowLevelInterface


def pos_class_factory(low_level_interface):

    class Pos(tuple):

        _lli = low_level_interface

        def __new__(cls, x, y, z):

            return tuple.__new__(cls, [x, y, z])

        def __str__(self):

            return 'Pos' + tuple.__str__(self)

            __repr__ = __str__

        # To implement player.pos += ... need PlayerPos class.
        def __iadd__(self, increment):

            if len(increment) != 3:
                raise ValueError

            return Pos(*tuple(
                a + b
                for a, b in zip(self, increment)
            ))

        @property
        def block(self):

            return self._lli.get_block(*map(int, self))


    return Pos



class Player:

    def __init__(self, world):

        self._world = world


    @property
    def pos(self):

        world = self._world
        lli = world._lli

        lli_pos = lli.player_get_pos()
        return world.Pos(*lli_pos)


    def move(self, vector):

        set_pos = self._world._lli.player_set_pos

        set_pos(*tuple(
            a + b
            for a, b in zip(self.pos, vector)
        ))


def world_factory(low_level_interface):

    lli = low_level_interface
    get_block = lli.get_block
    set_block = lli.set_block
    player_get_pos = lli.player_get_pos
    player_set_pos = lli.player_set_pos


    # Unless World has data it is not a class.

    class World:

        def __init__(self):

            self.player = Player()


        @staticmethod
        def __getitem__(key):

            return get_block(*key)

        @staticmethod
        def __setitem__(key, value):

            argv = list(key)
            argv.append(value)
            set_block(*argv)


    class Player:

        @property
        def pos(self):

            return player_get_pos()


        @staticmethod
        def goto(pos):

            player_set_pos(*map(float, pos))


        def move(self, vector):

            set_pos = self._world._lli.player_set_pos

            set_pos(*tuple(
                a + b
                for a, b in zip(self.pos, vector)
            ))



    return World()
