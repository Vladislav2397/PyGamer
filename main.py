from typing import Union

import pygame
from pygame.locals import (
    KEYDOWN, QUIT
)
from pygame import display
from pygame.time import Clock

from time import time

from common.config import (
    WINDOW_SIZE,
    FPS, TIMEOUT,
)
from common.base_game import BaseGame
from pySnake.main_menu import MainMenu
from pySnake.game import SnakeGame


# TODO: Add debug mode (optional)
# TODO: Add the end of the game =>
# TODO: => if the snake eats itself
# TODO: Reorganized and cleaning classes
# TODO: Write tests for classes


class Game:
    """ Base class of game """
    game: Union[BaseGame, None] = SnakeGame()
    main_menu = MainMenu()

    def __init__(self, window_size: tuple = None) -> None:
        """ Initialize of 'GAME' object """
        pygame.init()

        self._window = display.set_mode(window_size or WINDOW_SIZE)
        self._width, self._height = self._window.get_size()
        self._is_play = True
        self._timer = time()
        self._time = Clock()

    def run(self) -> None:
        """ Run main loop of game """
        self._time.tick(FPS)

        while self._is_play:
            self._check_events()
            if self.is_time:
                self.game.run()
                # self.main_menu.run()
                # self.main_menu.draw(self._window)
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
        if self.main_menu.is_close:
            self.close()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                self.close()
            elif event.type == KEYDOWN:
                if self.main_menu.check_events:
                    self.main_menu.check_events(event)
    
    def close(self) -> None:
        """ Close main loop of game """
        self._is_play = False

    def __del__(self) -> None:
        """ The exit from game """
        print("Exit from PyGamer")
        pygame.quit()


if __name__ == "__main__":
    Game().run()
