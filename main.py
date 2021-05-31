import pygame
from pygame.locals import QUIT
from pygame.display import flip

from common.tools import SingletonMeta

from common.config import MAIN_WINDOW_SURFACE

from common.frames.frame import Frame
# from pySnake.game_frame import SnakeGameFrame
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

# May be I need a app manager class as command receiver

# SOLID:

# - Single Responsible Principle (Принцип единой ответственности)
# - Open/Close Principle (Принцип открытости/закрытости)
# - Liskov Substitution Principle (Принцип подстановки Лисков)
# - Interface Segregation Principle (Принцип разделения интерфейса)
# - Dependency Inversion Principle (Принцип инверсии зависимостей)


class Application(metaclass=SingletonMeta):

    is_enabled = True
    is_pause = False
    _window = MAIN_WINDOW_SURFACE
    _main_frame = MainMenuFrame()

    def __del__(self) -> None:
        """ The exit from game """

        print("Exit from PyGamer")
        pygame.quit()

    def set_frame(self, frame: Frame):
        self._main_frame = frame

    def run(self):
        """ Started main loop of application """
        while self.is_enabled and not self.is_pause:
            self.update()
            self.draw()
            flip()

    def update(self):
        """ Check events and update data """

        events = pygame.event.get()

        for event in events:
            if event.type == QUIT:
                self.stop()

        self._main_frame.update(events)

    def draw(self):
        """ Draw one frame per second on window """

        self._main_frame.draw(self._window)

    def pause(self):
        self.is_pause = True

    def resume(self):
        self.is_pause = False

    def stop(self):
        """ Stopped main loop of application """
        self.is_enabled = False


if __name__ == "__main__":
    from manager import ApplicationManager

    ApplicationManager().run()
