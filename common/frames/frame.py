from abc import ABC, abstractmethod

from pygame_menu.menu import Menu

from common.config import MAIN_WINDOW_SURFACE


class Frame(ABC):
    @abstractmethod
    def update(self, events):
        raise NotImplementedError(
            'Обязательна реализация метода update'
        )

    @abstractmethod
    def draw(self, window):
        raise NotImplementedError(
            'Обязательна реализация метода draw'
        )


class HasParentMixin:
    def __init__(self, parent_frame):
        self._parent_frame = parent_frame

    @property
    def parent(self) -> Frame:
        return self._parent_frame


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
