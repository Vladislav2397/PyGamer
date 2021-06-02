from common.commands.command import CommandBase, GetFrameMixin


class StartGameCommand(CommandBase, GetFrameMixin):
    from manager import ApplicationManager

    _manager = ApplicationManager()

    def execute(self):
        self._manager.set_frame(self._frame)


class PauseGameCommand(CommandBase, GetFrameMixin):
    from manager import ApplicationManager

    _manager = ApplicationManager()

    def execute(self):
        self._manager.set_frame(self._frame)
