from common.frames.menu_frame import MenuFrame, Surface

from common.command import BackCommand


class SettingsMenuFrame(MenuFrame):

    def __init__(self, parent_window: Surface):
        super().__init__(parent_window, 'Settings')
        self.menu.add.selector(
            'Speed',
            [(str(i), i) for i in range(1, 6)]
        )
        self.menu.add.button('Save', BackCommand().execute())
