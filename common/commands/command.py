from abc import ABC, abstractmethod


class CommandBase(ABC):
    """
    Abstract class (interface) for application menu commands
    (Command pattern)
    """

    def __call__(self, *args, **kwargs):
        self.execute()

    @abstractmethod
    def execute(self):
        raise NotImplementedError(
            'Обязательно создание метода или свойства execute'
        )


class GetFrameMixin:
    def __init__(self, frame):
        self._frame = frame

