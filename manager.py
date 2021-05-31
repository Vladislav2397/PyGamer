class ApplicationManager:
    """ Manager for application (Receiver commands) """
    from main import Application

    _app = Application()

    def run(self):
        self._app.run()

    def stop(self):
        self._app.stop()

    def toggle_pause(self):
        if self._app.is_pause:
            self._app.resume()
        else:
            self._app.pause()

    def set_frame(self, frame):
        self._app.set_frame(frame)

    # Example
    # commands = {
    #     'draw main menu': DrawMainMenuCommand()
    # }

    # def __init__(self):
    #     self._app = Application()

    # def execute_command(self, command_name):
    #     self.commands[command_name].execute()
