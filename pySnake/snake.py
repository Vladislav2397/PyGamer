from typing import NamedTuple

from collections import deque
from pygame.sprite import Group
from pygame import Color

from common.config import (
    BLOCK_SIZE,
    LEFT, RIGHT, UP, DOWN,
    WINDOW_SIZE, MoveDirection
)
from common.position import Position
from common.other import BaseColor
from common.block import Block
from pySnake.helpers import colored_block_factory, next_block_position

Window = NamedTuple('window', [('width', int), ('height', int)])

green_block_factory = colored_block_factory()


class Snake(Group):
    """ Class for game object 'Snake' """
    
    def __init__(
        self,
        pos: list = None,
        color: Color = BaseColor.GREEN,
        window_size: tuple = WINDOW_SIZE,
        vector: str = RIGHT,
        *sprites
    ) -> None:
        """ Initialize snake """
        
        self._pos = Position(*pos or (BLOCK_SIZE * 5, BLOCK_SIZE * 4))
        if window_size:
            self.window = Window(*window_size)
        else:
            self.window = Window(100, 100)
        self._color = color
        self.vector = vector
        self._step = BLOCK_SIZE
        self._is_changed = False
        self._is_upgrade = False
        x, y = self._pos

        block_factory = colored_block_factory(self._color)

        self._body = deque([
            block_factory(x, y),
            block_factory(x - self._step, y),
            block_factory(x - self._step * 2, y),
        ])
        
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
    def next_position(self) -> Position:
        """ Return next position for snake """
        direction = None
        
        if self.vector == UP:
            direction = MoveDirection.UP
        elif self.vector == LEFT:
            direction = MoveDirection.LEFT
        elif self.vector == DOWN:
            direction = MoveDirection.DOWN
        elif self.vector == RIGHT:
            direction = MoveDirection.RIGHT

        return next_block_position(self.head, direction)

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
        elem.set_position(self._pos)
        self._body.appendleft(elem)
    
    def _upgrade_snake_body(self):
        """ Upgrade snake body """
        
        block = Block(pos=self._pos, color=self._color)
        self._body.appendleft(block)
        self.add(block)
    
    def _loop_in_frame(self):
        """ Check snake pos in frame and edit them """
        
        if self._pos.x < 0:
            self._pos.x = self.window.width - self._step
        elif self._pos.x >= self.window.width:
            self._pos.x = 0
        
        if self._pos.y < 0:
            self._pos.y = self.window.height - self._step
        elif self._pos.y >= self.window.height:
            self._pos.y = 0
    
    def move(self) -> None:
        """ Move snake by vector on one grid item """
        
        if self.vector == LEFT:
            self._pos = next_block_position(self.head, MoveDirection.LEFT)
        elif self.vector == RIGHT:
            self._pos = next_block_position(self.head, MoveDirection.RIGHT)
        elif self.vector == UP:
            self._pos = next_block_position(self.head, MoveDirection.UP)
        elif self.vector == DOWN:
            self._pos = next_block_position(self.head, MoveDirection.DOWN)
    
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
