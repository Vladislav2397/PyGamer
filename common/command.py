from abc import ABC, abstractmethod

from common.frames.menu_frame import MenuFrame

from pygame_menu.events import BACK, EXIT


class Command(ABC):
    """
    Abstract class for application menus commands
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


class SettingsCommand(Command):
    def __init__(self, settings_menu: MenuFrame):
        self.settings_menu = settings_menu

    def execute(self):
        return self.settings_menu.menu


class AboutCommand(Command):
    def __init__(self, about_menu: MenuFrame):
        self.about_menu = about_menu

    def execute(self):
        return self.about_menu.menu


class BackCommand(Command):
    def execute(self):
        return BACK


class QuitCommand(Command):
    def execute(self):
        return EXIT
