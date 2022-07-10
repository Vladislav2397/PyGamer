from enum import Enum

BLOCK_SIZE = 20
BLOCK_SIZE_TUPLE = (BLOCK_SIZE, BLOCK_SIZE)
WINDOW_SIZE = (
    BLOCK_SIZE * 25,
    BLOCK_SIZE * 25
)

FPS = 30
TIMEOUT = 0.2


class MoveDirection(Enum):
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'


LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'
CLOSE = 'close'
