from common.frames.menu_frame import MenuFrame

from common.command import BackCommand


class SettingsMenuFrame(MenuFrame):

    def __init__(self):
        super().__init__(title_menu='Settings')
        self.menu.add.selector(
            'Speed',
            [(str(i), i) for i in range(1, 6)]
        )
        self.menu.add.button('Save', BackCommand().execute())
