# Smoke test.  Should run without error.
# Main purpose of this file is to explore the API.

import minecraft
import minecraft.block as block

world = minecraft.connect(logging=True)

# Find the type of a block.
bt = world[0, 1, 2]             # At present, always UNKNOWN.
assert bt is block.UNKNOWN, bt

# Set the type of a block.
world[3, 4, 5] = block.DIRT

# Alternative way to set the type of block.
pos = (6, 7, 8)
world[pos] = block.AIR


assert world._log == [
    ('world.getBlock', (0, 1, 2), block.UNKNOWN),
    ('world.setBlock', (3, 4, 5), block.DIRT),
    ('world.setBlock', (6, 7, 8), block.AIR),
], world._log
