from time import time

import pygame
from pygame.time import Clock
from abc import ABC, abstractmethod


class BaseGame(ABC):
    def __init__(self):
        self._is_close = False
        self._timer = time()
        self._time = Clock()

    @property
    def timeout(self):
        return 0.2
    
    def run(self):
        pass
    
    @abstractmethod
    def check_events(self, event: pygame.event.Event):
        pass

    @abstractmethod
    def game_over(self):
        pass
    
    def close(self):
        self._is_close = True
