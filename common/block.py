from pygame.sprite import Sprite
from pygame import Surface, Color

from common.config import (BLOCK_SIZE, BLOCK_SIZE_TUPLE)
from common.other import MyColor
from common.position import Position


class Block(Sprite):
	""" Block sprite in game """

	def __init__(
		self,
		size: tuple = BLOCK_SIZE_TUPLE,
		pos: list = None,
		color: Color = MyColor.GREEN,
		*groups
	) -> None:
		""" Initalize block """

		super().__init__(*groups)
		if pos:
			self._pos = Position(pos)
		else:
			self._pos = Position([BLOCK_SIZE * 5, BLOCK_SIZE * 3])
		self._color = color
		self.image = Surface(size)
		self.image.fill(self._color)
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = self._pos

	def __str__(self) -> str:
		return str(self._pos)

	def set_position(self, pos: list) -> None:
		""" Set new position for block """

		if pos:
			self._pos = Position(pos)
			self.rect.x, self.rect.y = self._pos
		else:
			raise TypeError("Give uncorrect arguments")
