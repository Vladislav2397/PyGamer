from typing import Tuple
from abc import ABC, abstractmethod
from time import time

import pygame
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT,
    K_ESCAPE, KEYDOWN, QUIT
)
from pygame import display
from pygame.surface import Surface
from pygame.time import Clock
from pygame.sprite import Group, collide_rect

from pySnake.eat import Eat
from common.other import MyColor
from pySnake.snake import Snake
from common.config import (
    WINDOW_SIZE,
    LEFT, RIGHT, UP, DOWN,
    FPS, SPEED
)

# TODO: Add debug mode (optional)
# TODO: Add the end of the game =>
# TODO: => if the snake eats itself
# TODO: Reorganized and cleaning classes
# TODO: Write tests for classes


# As example:

# BaseMenu - Abstract class for all menu (main, pause)
# MainMenu and PauseMenu

# menu items - MenuItemCommand (pattern command)
# PlayCommand, PauseCommand, ChangeGameCommand, QuitCommand

# frame - frame for draw in app


class AllGroups(Group):
    """ Singleton for all groups """
    instance = set()


class Application:

    pygame.init()

    def __init__(
        self,
        window_size: tuple = None
    ) -> None:
        """ Initialize of 'Application' object """

        self._is_enabled = True
        self._display = display
        self._window = self._display.set_mode(window_size or WINDOW_SIZE)
        self._width, self._height = self._window.get_size()
        self.main_surface = MainMenu(self._window.get_size())

        while self._is_enabled:
            self._check_events()
            self.draw()
            self._display.flip()

    def _check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == QUIT:
                self.stop()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.stop()

    def draw(self):
        self.main_surface.run()
        self._window.blit(self.main_surface, (0, 0))

    def stop(self):
        self._is_enabled = False

    def __del__(self) -> None:
        """ The exit from game """

        print("Exit from PyGamer")
        pygame.quit()


class BaseMenu(ABC, Surface):
    pass


class MainMenu(BaseMenu):
    def __init__(self, size: Tuple[int, int]) -> None:
        """ Initialize of 'MainMenu' object with 'BaseMenu' interface """

        super().__init__(size)
        self._is_enabled = True
        self._timer = time()
        self._time = Clock()

    def _check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == QUIT:
                self.stop()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.stop()

    def run(self):
        self._check_events()
        self.draw()

    def draw(self):
        self.fill(MyColor.GREEN)

    def stop(self):
        self._is_enabled = False


class PauseMenu(BaseMenu):
    pass


class BaseGame(ABC):
    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError(
            'Обязательно создание метода run'
        )

    @abstractmethod
    def stop(self) -> None:
        raise NotImplementedError(
            'Обязательно создание метода close'
        )


class Game(BaseGame):
    """ Base class of game """

    def __init__(self, window_size: tuple = None) -> None:
        """ Initialize of 'GAME' object """

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
            display.flip()

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
        """ Close main loop of game """

        self._is_play = False


if __name__ == "__main__":
    Application()
