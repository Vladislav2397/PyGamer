from abc import ABC, abstractmethod

from pygame_menu.events import BACK


class CommandBase(ABC):
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


# class MenuDrawableMixin:
#     def __init__(self, menu):
#         from pygame_menu import Menu

#         if not isinstance(menu, Menu):
#             raise TypeError('type "menu" is not correct')


class StartGameCommand(CommandBase):
    def __init__(self):
        from pySnake.game_frame import SnakeGameFrame

        self._game = SnakeGameFrame()

    def execute(self):
        from main import Application

        Application().set_frame(self._game)


class PauseGameCommand(CommandBase):
    def __init__(self, game):
        self._game = game

    def execute(self):
        print(self._game)


class MainMenuCommand(CommandBase):
    def __init__(self):
        from common.frames.main_menu_frame import MainMenuFrame

        self.frame = MainMenuFrame().menu

    @property
    def execute(self):
        return self.frame


class SettingsMenuCommand(CommandBase):
    def __init__(self):
        from common.frames.settings_menu_frame import SettingsMenuFrame

        self.frame = SettingsMenuFrame().menu

    @property
    def execute(self):
        return self.frame


class AboutMenuCommand(CommandBase):
    def __init__(self):
        from common.frames.about_menu_frame import AboutMenuFrame

        self.frame = AboutMenuFrame().menu

    @property
    def execute(self):
        return self.frame


class BackCommand(CommandBase):
    def execute(self):
        return BACK


class QuitCommand(CommandBase):
    def execute(self):
        from main import Application

        Application().stop()
