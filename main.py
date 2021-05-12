from typing import Tuple
from abc import ABC, abstractmethod
from time import time

import pygame
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT,
    K_ESCAPE, KEYDOWN, QUIT
)
from pygame import display
from pygame.time import Clock
from pygame.sprite import Group, collide_rect

import pygame_menu
from pygame_menu import Menu

from common.command import (
    QuitCommand
)

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
# MainMenu, PauseMenu, SettingsMenu, AboutMenu
# or extends MenuAction

# menu items - MenuItemCommand (pattern command)
# PlayCommand, PauseCommand, SetGameCommand, AboutCommand, QuitCommand


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class AllSprites(Group, metaclass=SingletonMeta):
    """ Singleton for all sprites """
    pass


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
        self.main_surface.mainloop(self._window)
        self.menu = Menu('title', *self._window.get_size())

    def switch_menu(self):
        self.main_surface = Menu(
            'About',
            self._window.get_width(),
            self._window.get_height()
        )

    def __del__(self) -> None:
        """ The exit from game """

        print("Exit from PyGamer")
        pygame.quit()


class BaseMenu(ABC, Menu):
    pass


class MainMenu(BaseMenu):
    def __init__(self, size: Tuple[int, int], game=None) -> None:
        """ Initialize of 'MainMenu' object with 'BaseMenu' interface """

        super().__init__(
            title='Main Menu',
            width=size[0],
            height=size[1],
            center_content=True,
            theme=pygame_menu.themes.THEME_DARK
        )
        self._game = game() if game else Game()
        self._menu_items = [
            ('Start game', None),
            ('Settings', None),
            ('About', None),
            ('Quit', QuitCommand())
        ]
        self.add.selector('Select game', [('Snake', 1), ('Tetris', 2)])

        for title, command in self._menu_items:
            if command:
                self.add.button(
                    title=title,
                    action=command()
                )
            else:
                self.add.button(
                    title=title
                )

    def select_game(self):
        return self._game.run()


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
