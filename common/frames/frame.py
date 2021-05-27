from abc import ABC, abstractmethod

from pygame.surface import Surface
from pygame_menu.menu import Menu

from common.config import MAIN_WINDOW_SURFACE


class Frame(ABC):
    @abstractmethod
    def update(self, events):
        raise NotImplementedError(
            'Обязательна реализация метода update'
        )

    @abstractmethod
    def draw(self, parent_window):
        raise NotImplementedError(
            'Обязательна реализация метода draw'
        )


class MenuFrame(Frame):
    def __init__(self, title_menu: str):
        super().__init__(MAIN_WINDOW_SURFACE.get_size())
        self._menu = Menu(
            title_menu,
            MAIN_WINDOW_SURFACE.get_width(),
            MAIN_WINDOW_SURFACE.get_height()
        )

    def update(self, events):
        if self._menu.is_enabled():
            self._menu.update(events)

    def draw(self, parent_window):
        if self._menu.is_enabled():
            self._menu.draw(MAIN_WINDOW_SURFACE)


class GameFrame(Frame):
    def __init__(self):
        super().__init__(MAIN_WINDOW_SURFACE.get_size())
        self._frame = Surface(MAIN_WINDOW_SURFACE.get_size())

    def update(self, events):
        pass

    def draw(self, parent_window):
        pass
