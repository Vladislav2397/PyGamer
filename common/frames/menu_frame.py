from pygame_menu.menu import Menu
from pygame_menu.themes import THEME_DARK

from common.config import MAIN_WINDOW_SURFACE
from common.frames.frame import Frame


class MenuFrame(Frame):

    def __init__(self, title_menu: str):
        super().__init__()
        self._menu = Menu(
            title_menu,
            MAIN_WINDOW_SURFACE.get_width(),
            MAIN_WINDOW_SURFACE.get_height(),
            theme=THEME_DARK
        )

    @property
    def menu(self):
        return self._menu

    def update(self, events):
        if self._menu.is_enabled():
            self._menu.update(events)

    def draw(self, parent_window=None):
        if self._menu.is_enabled():
            self._menu.draw(parent_window or MAIN_WINDOW_SURFACE)
