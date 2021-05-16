from abc import ABC, abstractmethod
from time import time

import pygame
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN,
    K_ESCAPE, QUIT
)
from pygame.time import Clock
from pygame.display import set_mode, flip
from pygame.sprite import Group
from pygame.sprite import collide_rect

from common.config import (
    WINDOW_SIZE, FPS, SPEED,
    LEFT, RIGHT, UP, DOWN,
)
from common.tools import MyColor

from pySnake.snake import Snake
from pySnake.eat import Eat


class BaseGame(ABC):
    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError(
            'Обязательно создание метода run'
        )

    @abstractmethod
    def stop(self) -> None:
        raise NotImplementedError(
            'Обязательно создание метода stop'
        )


class Game(BaseGame):
    """ Base class of game """

    def __init__(self, window_size: tuple = None) -> None:
        """ Initialize of 'GAME' object """

        self._window = set_mode(window_size or WINDOW_SIZE)
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

    def run(self):
        """ Run main loop of game """

        self._time.tick(FPS)

        while self._is_play:
            self._check_events()
            self._all_groups.add([*self.snake.body, self.eat])
            if self.is_time:
                self.snake.move()
                self._check_colliderect()
                self.eat.update()
                self.snake.update()
                self._window.fill(MyColor.BLACK)
                self._all_groups.draw(self._window)
            flip()

    @property
    def is_time(self) -> bool:
        """ It's property return boolean if is timeout """

        if self._timer < time():
            self._timer = time() + SPEED
            return True
        return False

    def _check_events(self) -> None:
        """ Check all events and set action """
        for event in pygame.event.get():
            if event.type == QUIT:
                self.stop()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.stop()
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
            self.eat.upgrade(self.snake.get_positions)

    def stop(self) -> None:
        """ Stop main loop of game """
        self._is_play = False
