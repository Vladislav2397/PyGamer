from abc import ABC, abstractmethod

import pygame_menu.events
from pygame.locals import QUIT


class Command(ABC):
    def __call__(self, *args, **kwargs):
        self.execute()

    @abstractmethod
    def execute(self):
        raise NotImplementedError(
            'Обязательно создание метода execute'
        )


class StartGameCommand(Command):
    def __init__(self, game):
        self._game = game

    def execute(self):
        self._game.run()
        return 'game run'


class PauseGameCommand(Command):
    def __init__(self, game):
        self._game = game

    def execute(self):
        self._game.pause()
        return 'game pause'


class AboutCommand(Command):
    def __init__(self, about_menu):
        self._about_menu = about_menu
        self.execute = about_menu

    def execute(self):
        # return self._about_menu
        pass


class QuitCommand(Command):
    def __init__(self):
        self.execute = pygame_menu.events.EXIT

    def execute(self):
        pass
