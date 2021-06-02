from common.commands.command import CommandBase, GetFrameMixin
from abc import ABC

from pygame_menu.events import BACK


class MenuCommandBase(CommandBase, ABC):

    from common.frames.menu_frame import MenuFrame

    def __init__(self, frame: MenuFrame):
        super().__init__(frame)


class MainMenuCommand(MenuCommandBase, GetFrameMixin):
    def execute(self):
        return self._frame.menu


class SettingsMenuCommand(MenuCommandBase, GetFrameMixin):
    def execute(self):
        return self._frame.menu


class AboutMenuCommand(MenuCommandBase, GetFrameMixin):
    def execute(self):
        return self._frame.menu


class BackCommand(CommandBase):
    def execute(self):
        return BACK


class QuitCommand(CommandBase):
    def execute(self):
        from manager import ApplicationManager

        ApplicationManager().stop()
