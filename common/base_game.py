from time import time
from pygame.time import Clock
from abc import ABC, abstractmethod
from common.config import (FPS)


class BaseGame(ABC):
    def __init__(self):
        self._timer = time()
        self._time = Clock()

    @property
    def timeout(self):
        return 0.2
    
    def run(self):
        self._time.tick(FPS)

    @abstractmethod
    def game_over(self):
        pass
