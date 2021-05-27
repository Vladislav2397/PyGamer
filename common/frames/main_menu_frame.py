from pygame.locals import KEYDOWN, K_ESCAPE

from common.command import (
    StartGameCommand,
    SettingsMenuCommand,
    AboutMenuCommand,
    ExitCommand,
    QuitCommand
)

from common.frames.menu_frame import MenuFrame


class MainMenuFrame(MenuFrame):

    menu_content = {
        'Start game': StartGameCommand().execute,
        'Settings': SettingsMenuCommand().execute,
        'About': AboutMenuCommand().execute,
        'Quit': ExitCommand().execute()
    }

    def __init__(self):
        super().__init__(title_menu='MainMenu')

        self.menu.add.selector(
            'Select game',
            [('Snake', 1), ('Tetris', 2)]
        )
        for name, command in self.menu_content.items():
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
