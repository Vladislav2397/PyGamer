from pygame.locals import KEYDOWN, K_ESCAPE

from common.commands.menu_command import (
    SettingsMenuCommand,
    AboutMenuCommand,
    QuitCommand
)

from common.frames.settings_menu_frame import SettingsMenuFrame
from common.frames.about_menu_frame import AboutMenuFrame
# from common.commands.game_command import StartGameCommand

from common.frames.menu_frame import MenuFrame


class MainMenuFrame(MenuFrame):

    menu_content = {
        'Start game': None,
        'Settings': SettingsMenuCommand(SettingsMenuFrame()),
        'About': AboutMenuCommand(AboutMenuFrame()),
        'Quit': QuitCommand()
    }

    def __init__(self):
        super().__init__(title_menu='MainMenu')

        self.menu.add.selector(
            'Select game',
            [('Snake', 1), ('Tetris', 2)]
        )
        for name, command in self.menu_content.items():
            if command:
                self.menu.add.button(
                    name, command.execute
                )
            else:
                self.menu.add.button(
                    name, command
                )

    def update(self, events=None):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    QuitCommand().execute()
        super().update(events)

    def draw(self, parent_window=None):
        super().draw()
