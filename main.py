import pygame
from pygame.constants import K_SPACE
from pygame.locals import (
	K_UP, K_DOWN, K_LEFT, K_RIGHT,
	K_ESCAPE, KEYDOWN, QUIT
)
from pygame import display
from pygame.time import Clock

from time import time

from pygame.sprite import Group, collide_rect
from pySnake.eat import Eat
from common.other import MyColor
from pySnake.snake import Snake
from common.config import (
	WINDOW_SIZE,
	LEFT, RIGHT, UP, DOWN,
	FPS, TIMEOUT
)

# TODO: Add debug mode (optional)
# TODO: Add random change eat position
# * Don't collide with snake
# TODO: Reorganized and cleaning classes
# TODO: Write tests for classes


class Game:
	""" Base class of game """

	def __init__(self, window_size: tuple = None) -> None:
		""" Initalize of 'GAME' object """

		pygame.init()

		self._window = display.set_mode(window_size or WINDOW_SIZE)
		self._width, self._height = self._window.get_size()
		self._is_play = True
		self._timer = time()
		self._time = Clock()

		self.snake = Snake(
			color=MyColor.GREEN,
			window_size=(self._width, self._height)
		)
		self.eat = Eat(pos=[40, 20], color=MyColor.RED)
		self._all_groups = Group(self.snake, self.eat)

	def run(self) -> None:
		""" Run main loop of game """

		self._time.tick(FPS)

		while self._is_play:
			self._check_events()
			self._all_groups.add([*self.snake._body, self.eat])
			if self.is_time:
				self.snake.move()
				self._check_colliderect()
				self.eat.update()
				self.snake.update()
				self._window.fill(MyColor.BLACK)
				self._all_groups.draw(self._window)
			display.flip()

	@property
	def is_time(self) -> bool:
		""" It's property return boolean if is timeout """

		if self._timer < time():
			self._timer = time() + TIMEOUT
			return True
		return False
	
	def _check_events(self) -> None:
		""" Check all events and set action """
		for event in pygame.event.get():
			if event.type == QUIT:
				self.close()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					self.close()
				elif event.key == K_LEFT:
					self.snake.turn(LEFT)
				elif event.key == K_RIGHT:
					self.snake.turn(RIGHT)
				elif event.key == K_UP:
					self.snake.turn(UP)
				elif event.key == K_DOWN:
					self.snake.turn(DOWN)

	def _check_colliderect(self):
		""" Check has collide rect """

		hit = collide_rect(self.snake.head, self.eat)
		if hit:
			self.snake.upgrade()
			self.eat.upgrade()

	def close(self) -> None:
		""" Close main loop of game """

		self._is_play = False

	def __del__(self) -> None:
		""" The exit from game """

		print("Exit from PyGamer")
		pygame.quit()


if __name__ == "__main__":
	Game().run()
