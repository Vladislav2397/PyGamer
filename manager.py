import pygame

pygame.init()


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


if __name__ == "__main__":
    from common.tools import init_app

    init_app()
    app = ApplicationManager()
    app.run()
