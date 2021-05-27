from abc import ABC, abstractmethod

from pygame_menu.events import BACK, EXIT


class Command(ABC):
    """
    Abstract class (interface) for application menu commands
    (Command pattern)
    """

    def __call__(self, *args, **kwargs):
        self.execute()

    @abstractmethod
    def execute(self):
        raise NotImplementedError(
            'Обязательно создание метода или свойства execute'
        )


class StartGameCommand(Command):
    def __init__(self):
        from pySnake.game_frame import SnakeGameFrame

        self._game = SnakeGameFrame()

    def execute(self):
        from main import Application

        Application().set_surface(self._game)


class PauseGameCommand(Command):
    def __init__(self, game):
        self._game = game

    def execute(self):
        print(self._game)


class MainMenuCommand(Command):
    def __init__(self):
        from common.frames.main_menu_frame import MainMenuFrame

        self.frame = MainMenuFrame().menu

    @property
    def execute(self):
        return self.frame


class SettingsMenuCommand(Command):
    def __init__(self):
        from common.frames.settings_menu_frame import SettingsMenuFrame

        self.frame = SettingsMenuFrame().menu

    @property
    def execute(self):
        return self.frame


class AboutMenuCommand(Command):
    def __init__(self):
        from common.frames.about_menu_frame import AboutMenuFrame

        self.frame = AboutMenuFrame().menu

    @property
    def execute(self):
        return self.frame


class BackCommand(Command):
    def execute(self):
        return BACK


class ExitCommand(Command):
    def execute(self):
        return EXIT


class QuitCommand(Command):
    def execute(self):
        from main import Application

        Application().stop()
