from common.frames.menu_frame import MenuFrame


class AboutMenuFrame(MenuFrame):

    def __init__(self, application):
        super().__init__(application, title_menu='About')
        self._menu.add.label(
            'Created by GlaDiatoR2397\n'
            '14.05.2021'
        )
