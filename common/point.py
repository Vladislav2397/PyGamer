from collections import UserList


class Point(UserList):
    """ Class point for 'Snake' object """

    def __init__(
            self,
            pos: list = None,
    ) -> None:
        """ Initialize 'Point' object """

        if pos and len(pos) == 2:
            self.data = list(pos)
        else:
            raise TypeError(
                "Atribute class Position can get "
                "only list with 2 items"
            )

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

    def set_position(self, pos) -> None:
        """ Set position """
        if isinstance(pos, Point):
            self.data = list(pos.data)
        else:
            self.data = list(pos)
