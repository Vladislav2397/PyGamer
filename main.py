import pygame
from pygame.locals import (
    K_ESCAPE, KEYDOWN, QUIT
)
from pygame import display

from common.config import (
    WINDOW_SIZE
)

from common.tools import Window

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


class Application:

    pygame.init()

    def __init__(self) -> None:
        """ Initialize of 'Application' object """

        self._is_enabled = True
        self._window = display.set_mode(Window().size or WINDOW_SIZE)
        self._width, self._height = self._window.get_size()

        self.main_surface = MainMenuFrame(self._window)

        self.run()

    def run(self):
        while self._is_enabled:
            self.draw()
            display.flip()

    def draw(self):
        events = pygame.event.get()

        for event in events:
            if event.type == QUIT:
                self.stop()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.stop()

        self.main_surface.loop(events)

    def stop(self):
        self._is_enabled = False

    def __del__(self) -> None:
        """ The exit from game """

        print("Exit from PyGamer")
        pygame.quit()


class SnakeGameFrame:
    pass


if __name__ == "__main__":
    Application()
