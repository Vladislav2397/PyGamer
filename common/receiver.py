from main import Application

from common.tools import SingletonMeta


class ApplicationReceiver(metaclass=SingletonMeta):
    app = Application()

    def set_frame(self, frame):
        self.app.set_frame(frame)
