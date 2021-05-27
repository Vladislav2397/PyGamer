from common.tools import SingletonMeta

from common.command import (
    MainMenuCommand,
    AboutMenuCommand,
    SettingsMenuCommand,
    StartGameCommand,
    PauseGameCommand
)

from common.receiver import ApplicationReceiver


class ApplicationInvoker(metaclass=SingletonMeta):

    receiver = ApplicationReceiver()

    def __init__(
        self,
        main_menu_command: MainMenuCommand,
        about_menu_command: AboutMenuCommand,
        settings_menu_command: SettingsMenuCommand,
        start_game_command: StartGameCommand,
        pause_game_command: PauseGameCommand,
    ):
        self.main_menu = MainMenuCommand()
        self.about_menu = AboutMenuCommand()
        self.settings_menu = SettingsMenuCommand()
        self.start_game = StartGameCommand()
        self.pause_game = PauseGameCommand()

    def set_main_menu(self):
        self.receiver.set_frame(self.main_menu)
