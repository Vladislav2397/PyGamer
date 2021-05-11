from collections import UserList


class Position(UserList):
    """ Class position for 'Snake' object """

    def __init__(
        self,
        pos: list = None,
        step: int = 0
    ) -> None:
        """ Initialize 'Position' object """

        super().__init__()
        if pos and len(pos) == 2:
            self.data = list(pos)
        else:
            raise TypeError(
                "Attribute class Position can get "
                "only list with 2 items"
            )
        self._step = step

    @property
    def x(self) -> int:
        """ Readonly field x """
        return self.data[0]

    @property
    def y(self) -> int:
        """ Readonly field y """
        return self.data[1]

    @x.setter
    def x(self, value: int) -> None:
        """ Set field x """
        self.data[0] = value

    @y.setter
    def y(self, value: int) -> None:
        """ Set field y """
        self.data[1] = value

    @property
    def get_left(self) -> tuple:
        """ Get left position """
        return self.x - self._step, self.y

    @property
    def get_right(self) -> tuple:
        """ Get right position """
        return self.x + self._step, self.y

    @property
    def get_top(self) -> tuple:
        """ Get top position """
        return self.x, self.y - self._step

    @property
    def get_bottom(self) -> tuple:
        """ Get bottom position """
        return self.x, self.y + self._step

    def set_position(self, pos: list) -> None:
        """ Set position """
        self.data = list(pos)

    def move_left(self) -> None:
        """ Move position on one step left """
        self.data[0] -= self._step

    def move_right(self) -> None:
        """ Move position on one step right """
        self.data[0] += self._step

    def move_top(self) -> None:
        """ Move position on one step top """
        self.data[1] -= self._step

    def move_bottom(self) -> None:
        """ Move position on one step bottom """
        self.data[1] += self._step
