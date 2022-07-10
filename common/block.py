from typing import Union

from pygame.sprite import Sprite
from pygame import Surface, Color

from common.config import (BLOCK_SIZE, BLOCK_SIZE_TUPLE)
from common.other import BaseColor
from common.position import Position


class Block(Sprite):
    """ Block sprite in game """

    def __init__(
            self,
            size: tuple = BLOCK_SIZE_TUPLE,
            pos: Union[list, Position] = None,
            color: Color = BaseColor.GREEN,
            *groups
    ) -> None:
        """ Initialize block """

        super().__init__(*groups)
        
        self._point = Position(pos or [BLOCK_SIZE * 5, BLOCK_SIZE * 3])
        self._color = color
        self.image = Surface(size)
        self.image.fill(BaseColor.BLACK)
        self.image.fill(self._color, self.image.get_rect().inflate(-2, -2))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self._point

    def __repr__(self) -> str:
        return f"Block {self._point} {self._color}"

    @property
    def get_pos(self):
        """ Return block position """
        return self._point

    @property
    def x(self):
        return self.rect.x

    @property
    def y(self):
        return self.rect.y
    
    @property
    def position(self):
        return self._point
    
    @property
    def size(self):
        return BLOCK_SIZE

    def set_position(self, pos: Union[list, Position]) -> None:
        """ Set new position for block """

        point = Position(pos)
        if point:
            self._point = point
        else:
            raise TypeError("Give incorrect arguments")

        self.rect.x, self.rect.y = self._point
