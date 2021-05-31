from typing import Tuple, NamedTuple

from pygame.sprite import Group
from pygame.color import Color

from common.config import WINDOW_SIZE


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class AllSprites(Group, metaclass=SingletonMeta):
    """ Singleton for all sprites """
    pass


class Window(NamedTuple):
    """ Application window size namedtuple """
    width: int = WINDOW_SIZE[0]
    height: int = WINDOW_SIZE[1]

    @property
    def size(self) -> Tuple[int, int]:
        """
        :return: Tuple width and height window
        """
        return self.width, self.height


class MyColor(NamedTuple):
    """
    Common colors for application
    """

    BLACK = Color(0, 0, 0)
    WHITE = Color(255, 255, 255)
    GREY = Color(127, 127, 127)
    RED = Color(255, 0, 0)
    GREEN = Color(0, 255, 0)
    BLUE = Color(0, 0, 255)

    DARKBLUE = Color(0, 0, 139)
    DIMGRAY = Color(105, 105, 105)

    WHITESMOKE = Color(245, 245, 245)
