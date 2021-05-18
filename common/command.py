from abc import ABC, abstractmethod

from pygame_menu.events import BACK, EXIT

from common.receiver import ApplicationReceiver

from common.frames.menu_frame import MenuFrame


class Command(ABC):
    """
    Abstract class for application menu commands
    (Command pattern)
    """

    receiver = ApplicationReceiver()

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
        return self._execute

    def _execute(self):
        self._game.set_as_main_surface()


class PauseGameCommand(Command):
    def __init__(self, game):
        self._game = game

    def execute(self):
        self._game.pause()
        return 'game pause'


class MainMenuCommand(Command):
    def __init__(self, main_menu: MenuFrame):
        self.main_menu = main_menu

    def execute(self):
        # TODO: Set main surface for application
        return 'Success'


class SettingsMenuCommand(Command):
    def __init__(self, settings_menu: MenuFrame):
        self.settings_menu = settings_menu

    def execute(self):
        return self.settings_menu.menu


class AboutMenuCommand(Command):
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
