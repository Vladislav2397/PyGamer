from abc import ABC, abstractmethod


class Frame(ABC):
    @abstractmethod
    def update(self, events):
        raise NotImplementedError(
            'Обязательна реализация метода update'
        )

    @abstractmethod
    def draw(self, window):
        raise NotImplementedError(
            'Обязательна реализация метода draw'
        )
