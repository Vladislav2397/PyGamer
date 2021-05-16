from common.frames.menu_frame import MenuFrame, Surface


class AboutMenuFrame(MenuFrame):

    def __init__(self, parent_window: Surface):
        super().__init__(parent_window, 'About')
        self._menu.add.label(
            'Created by GlaDiatoR2397\n'
            '14.05.2021'
        )
