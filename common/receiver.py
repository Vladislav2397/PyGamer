from main import Application

from common.tools import SingletonMeta


class ApplicationReceiver(metaclass=SingletonMeta):
    app = Application()
