from pygame.surface import Surface
from pygame_menu.menu import Menu
from pygame_menu.themes import THEME_DARK

from common.tools import Window


class MenuFrame(Surface):

    def __init__(self, application, title_menu: str):
        window = Window()
        super().__init__(window)
        self._app = application
        self._menu = Menu(
            title_menu,
            window.width,
            window.height,
            theme=THEME_DARK
        )

    @property
    def menu(self):
        return self._menu

    def loop(self, events):
        if self._menu.is_enabled():
            self._menu.update(events)
            self._menu.draw(self._app.window)
