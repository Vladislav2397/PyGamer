from common.command import (
    SettingsCommand,
    AboutCommand,
    QuitCommand
)

from common.frames.menu_frame import MenuFrame, Surface
from common.frames.about_menu_frame import AboutMenuFrame
from common.frames.settings_menu_frame import SettingsMenuFrame


class MainMenuFrame(MenuFrame):

    def __init__(self, parent_window: Surface):
        super().__init__(parent_window, title_menu='MainMenu')

        about_menu = AboutMenuFrame(self._parent)
        settings_menu = SettingsMenuFrame(self._parent)

        self._menu.add.selector(
            'Select game',
            [('Snake', 1), ('Tetris', 2)]
        )
        self._menu.add.button(
            'Start game',
            None
        )
        self._menu.add.button(
            'Settings',
            SettingsCommand(settings_menu).execute()
        )
        self._menu.add.button(
            'About',
            AboutCommand(about_menu).execute()
        )
        self._menu.add.button(
            'Quit',
            QuitCommand().execute()
        )
