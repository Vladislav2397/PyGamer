from typing import Union

from pygame.sprite import Sprite
from pygame import Surface, Color

from common.config import (BLOCK_SIZE, BLOCK_SIZE_TUPLE)
from common.other import MyColor
from common.position import Position
from common.point import Point


class Block(Sprite):
    """ Block sprite in game """

    def __init__(
            self,
            size: tuple = BLOCK_SIZE_TUPLE,
            pos: Union[list, Point] = None,
            color: Color = MyColor.GREEN,
            *groups
    ) -> None:
        """ Initalize block """

        super().__init__(*groups)
        if pos:
            if isinstance(pos, Point):
                self._point = pos
            else:
                self._point = Point(pos)
        else:
            self._point = Point([BLOCK_SIZE * 5, BLOCK_SIZE * 3])
        self._color = color
        self.image = Surface(size)
        self.image.fill(self._color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self._point

    def __repr__(self) -> str:
        return f"Block {self._point}"

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

    def set_position(self, pos: Union[list, Point]) -> None:
        """ Set new position for block """

        if pos:
            if isinstance(pos, Point):
                self._point = pos
            else:
                self._point = Position(pos)

            self.rect.x, self.rect.y = self._point
        else:
            raise TypeError("Give uncorrect arguments")
