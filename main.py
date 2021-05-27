import pygame
from pygame.locals import QUIT
from pygame.display import flip
from pygame.surface import Surface

from common.tools import SingletonMeta

from common.config import MAIN_WINDOW_SURFACE

from common.frames.main_menu_frame import MainMenuFrame
# from pySnake.game_frame import SnakeGameFrame

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

# Command manager
# CommandInvoker -> Command => CommandReceiver

# Adapter for pygame menu

# SOLID:

# - Single Responsible Principle (Принцип единой ответственности)
# - Open/Close Principle (Принцип открытости/закрытости)
# - Liskov Substitution Principle (Принцип подстановки Лисков)
# - Interface Segregation Principle (Принцип разделения интерфейса)
# - Dependency Inversion Principle (Принцип инверсии зависимостей)


class Application(metaclass=SingletonMeta):

    def __init__(self) -> None:
        """ Initialize of 'Application' object """

        self._is_enabled = True
        self._window = MAIN_WINDOW_SURFACE
        self.main_frame = MainMenuFrame()

    def __del__(self) -> None:
        """ The exit from game """

        print("Exit from PyGamer")
        pygame.quit()

    def set_surface(self, surface: Surface):
        self.main_frame = surface

    def run(self):
        """ Started main loop of application """
        while self._is_enabled:
            self.update()
            self.draw()
            flip()

    def update(self):
        """ Check events and update data """

        events = pygame.event.get()

        for event in events:
            if event.type == QUIT:
                self.stop()

        self.main_frame.update(events)

    def draw(self):
        """ Draw one frame per second on window """

        self.main_frame.draw(self._window)

        # self.main_surface.draw()

    def stop(self):
        """ Stopped main loop of application """
        self._is_enabled = False


if __name__ == "__main__":
    Application().run()
