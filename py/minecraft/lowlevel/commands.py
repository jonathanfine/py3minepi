'''Commands for the low-level interface

This module, indirectly, defines all the commands available in the
low-level interface.  More exactly, it contains the data that is used
to build the low-level interface commands.

Five pieces of information are stored for each low-level command.

#. The Python name of the command.
#. The input signature for the command.
#. The output signature for the command.
#. The docstring for the command.

These five pieces of information we call the *signature* for the
command.  The signature determines the serialisation of the command
and its arguments, and the deserialisation of its return value.

The command_builder function (in the lowlevel.tools module) constructs
the Python command from its signature.  The simplicity of the
signature means that all the complication has been moved elsewhere,
mainly to the command_builder.

Some commands provided by Minecraft have alternate forms, with
different input signatures.

'''

SIGNATURES = dict(

    ## Block commands.
    set_block = (
        'world.setBlock',
        [int, int, int, int], None,
        '''Set block type at location (xi, yi, zi).

        world.setBlock(x, y, z, blockTypeId)
        '''
    ),

    set_block2 = (
        'world.setBlock',
        [int, int, int, int, int], None,
        '''Set block type and extra data at location (xi, yi, zi).

        world.setBlock(x, y, z, blockTypeId, blockData)
        '''
    ),

    get_height = (
        'world.getHeight',
        [int, int, int], int,
        '''Return world's height at location (xi, yi, zi).

        world.getHeight(x,z) --> Integer
        '''
    ),

    ## Player commands.
    player_get_pos = (
        'player.getPos',
        None, [float, float, float],
        '''Return (xf, yf, zf), the player's current position.

        player.getPos() --> xf, yf, zf
        '''
    ),

    player_set_pos = (
        'player.setPos',
        [float, float, float], None,
        '''Set the player's current position to (xf, yf, zf).

        player.setPos(xf, yf, zf)
        '''
    ),
)
