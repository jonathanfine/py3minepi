class _BlockType(str):

    def __repr__(self):
        return 'blocks.' + self

    __str__ = __repr__


AIR = _BlockType('AIR')
STONE = _BlockType('STONE')
