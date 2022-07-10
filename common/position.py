from collections import UserList


def to_position_tuple(*pos):
    if pos and len(pos) == 2:
        return pos
    elif isinstance(pos[0], Position):
        return pos[0]
    elif len(pos[0]) == 2:
        return pos[0]
    else:
        raise TypeError("Position initialize get not correct arguments")


class Position(UserList):
    """ Class position for Block object """
    
    def __init__(
        self,
        *pos: list,
    ) -> None:
        """ Initialize """
        
        super().__init__(to_position_tuple(*pos))
    
    @property
    def x(self) -> int:
        """ Readonly position field x """
        return self.data[0]
    
    @property
    def y(self) -> int:
        """ Readonly position field y """
        return self.data[1]
    
    @x.setter
    def x(self, value: int) -> None:
        """ Set position field x """
        self.data[0] = value
    
    @y.setter
    def y(self, value: int) -> None:
        """ Set position field y """
        self.data[1] = value
    
    def set_position(self, pos: list) -> None:
        """ Set position fields """
        self.data = list(pos)
        
    def __add__(self, other):
        self.set_position(to_position_tuple(*other))
