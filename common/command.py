from abc import ABC, abstractmethod

import pygame_menu


class Command(ABC):
    def __call__(self, *args, **kwargs):
        return self.execute()

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


class PauseGameCommand(Command):
    def __init__(self, game):
        self._game = game

    def execute(self):
        self._game.pause()


class AboutCommand(Command):
    def __init__(self, about_menu):
        self._about_menu = about_menu

    def execute(self):
        return self._about_menu


class QuitCommand(Command):
    def execute(self):
        return pygame_menu.events.EXIT
