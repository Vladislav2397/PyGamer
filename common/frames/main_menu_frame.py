from common.command import (
    SettingsCommand,
    AboutCommand,
    QuitCommand
)

from common.frames.menu_frame import MenuFrame
from common.frames.about_menu_frame import AboutMenuFrame
from common.frames.settings_menu_frame import SettingsMenuFrame


class MainMenuFrame(MenuFrame):

    def __init__(self, application):
        super().__init__(application, title_menu='MainMenu')

        about_menu = AboutMenuFrame(application)
        settings_menu = SettingsMenuFrame(application)

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
