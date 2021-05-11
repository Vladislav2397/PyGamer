from common.config import WINDOW_SIZE, BLOCK_SIZE
from common.block import Block
from random import choice


class Eat(Block):

    def __init__(self, pos: list, color: tuple, *groups) -> None:
        _positions = range(0, WINDOW_SIZE[0], BLOCK_SIZE)
        self.positions = set(
            (x, y)
            for x in _positions
            for y in _positions
        )
        super().__init__(pos=pos, color=color, *groups)

    def upgrade(self, snake_pos: set):
        pos = choice(list(self.positions - snake_pos))
        self.set_position(list(pos))
