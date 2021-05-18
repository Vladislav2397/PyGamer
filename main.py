import pygame
from pygame.locals import QUIT
from pygame.display import set_mode, flip
from pygame.surface import Surface

from common.config import (
    WINDOW_SIZE
)

from common.tools import Window, SingletonMeta

from common.frames.main_menu_frame import MainMenuFrame

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


class Application(metaclass=SingletonMeta):

    pygame.init()

    def __init__(self) -> None:
        """ Initialize of 'Application' object """

        self._is_enabled = True
        self._window = set_mode(Window().size or WINDOW_SIZE)

        self.main_surface = None

        self.run()

    def __del__(self) -> None:
        """ The exit from game """

        print("Exit from PyGamer")
        pygame.quit()

    @property
    def window(self):
        return self._window

    def set_surface(self, surface: Surface):
        self.main_surface = surface

    def run(self):
        """ Started main loop of application """
        while self._is_enabled:
            self.draw()
            flip()

    def draw(self):
        """ Draw one frame per second on window """
        events = pygame.event.get()

        for event in events:
            if event.type == QUIT:
                self.stop()

        self.main_surface.loop(events)

    def stop(self):
        """ Stopped main loop of application """
        self._is_enabled = False


if __name__ == "__main__":
    Application()
