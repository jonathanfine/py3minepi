class _BlockType(str):

    def __repr__(self):
        return 'block.' + self


AIR = _BlockType('AIR')
DIRT = _BlockType('DIRT')
GRASS = _BlockType('GRASS')
STONE = _BlockType('STONE')

UNKNOWN = _BlockType('UNKNOWN')
