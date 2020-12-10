from common.config import WINDOW_SIZE, BLOCK_SIZE
from common.block import Block
from random import choice


positions = list(range(0, WINDOW_SIZE[0], BLOCK_SIZE))


class Eat(Block):
	
	def __init__(self, pos: list, color: tuple, *groups) -> None:
		super().__init__(pos=pos, color=color, *groups)
	
	def upgrade(self):
		self.set_position(
			[choice(positions), choice(positions)]
		)