from typing import NamedTuple
from collections import deque

from pygame.sprite import Group
from pygame import Color

from common.config import (
    BLOCK_SIZE,
    LEFT, RIGHT, UP, DOWN
)
from common.position import Position
from common.other import MyColor
from common.block import Block

Window = NamedTuple('window', [('width', int), ('height', int)])


class Snake(Group):
    """ Class for game object 'Snake' """

    def __init__(
        self,
        pos: list = None,
        window_size: tuple = None,
        color: Color = MyColor.GREEN,
        vector: str = RIGHT,
        *sprites
    ) -> None:
        """ Initialize snake """

        if pos:
            self.pos = Position(pos, step=BLOCK_SIZE)
        else:
            self.pos = Position(
                [BLOCK_SIZE * 5, BLOCK_SIZE * 4],
                step=BLOCK_SIZE
            )
        if window_size:
            self.window = Window(*window_size)
        else:
            self.window = Window(100, 100)
        self._color = color
        self.vector = vector
        self._step = BLOCK_SIZE
        self._is_changed = False
        self._is_upgrade = False
        x, y = self.pos
        self._body = deque(
            [
                Block(pos=(x, y), color=self._color),
                Block(pos=(x - self._step, y), color=self._color),
                Block(pos=(x - self._step * 2, y), color=self._color)
            ]
        )
        super().__init__([*sprites, *self._body])

    def __len__(self) -> int:
        return len(self._body)

    @property
    def head(self) -> Block:
        """ Get head block """
        return self._body[0]

    @property
    def length(self) -> int:
        """ Get length snake """
        return len(self)

    @property
    def get_positions(self) -> set:
        """ Get all positions snake body """

        return set([(block.x, block.y) for block in self._body])

    @property
    def body(self):
        return self._body

    def _update_vector(self, vector: str) -> None:
        """ Change vector snake """

        if vector == LEFT and self.vector != RIGHT:
            self.vector = LEFT
        elif vector == RIGHT and self.vector != LEFT:
            self.vector = RIGHT
        elif vector == UP and self.vector != DOWN:
            self.vector = UP
        elif vector == DOWN and self.vector != UP:
            self.vector = DOWN

    def _update_snake_body(self):
        """ Update snake body """

        elem = self._body.pop()
        elem.set_position(self.pos)
        self._body.appendleft(elem)

    def _upgrade_snake_body(self):
        """ Upgrade snake body """

        block = Block(pos=self.pos, color=self._color)
        self._body.appendleft(block)
        self.add(block)

    def _loop_in_frame(self):
        """ Check snake pos in frame and edit them """

        if self.pos.x < 0:
            self.pos.x = self.window.width - self._step
        elif self.pos.x >= self.window.width:
            self.pos.x = 0

        if self.pos.y < 0:
            self.pos.y = self.window.height - self._step
        elif self.pos.y >= self.window.height:
            self.pos.y = 0

    def move(self) -> None:
        """ Move snake by vector on one grid item """

        if self.vector == LEFT:
            self.pos.move_left()
        elif self.vector == RIGHT:
            self.pos.move_right()
        elif self.vector == UP:
            self.pos.move_top()
        elif self.vector == DOWN:
            self.pos.move_bottom()

    def turn(self, vector: str) -> None:
        """ Check and update snake vector """

        if not self._is_changed:
            self._is_changed = True
            self._update_vector(vector)

    def update(self, *args, **kwargs) -> None:
        """ Update position snake """

        self._is_changed = False
        self._loop_in_frame()
        self._update_snake_body()
        super().update(*args, **kwargs)

    def upgrade(self):
        """ Update length snake """
        self._upgrade_snake_body()
