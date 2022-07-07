import pygame.event

from common.config import WINDOW_SIZE


class Frame:
    def __init__(self):
        self._is_close = False
        self._window = pygame.display.set_mode(WINDOW_SIZE)
    
    def draw(self):
        pass

    def check_events(self, event: pygame.event.Event):
        pass
    
    @property
    def is_close(self):
        return self._is_close
    
    @property
    def timeout(self):
        return 0.2

    def close(self):
        self._is_close = True


class Config:
    _frame = None
    
    @property
    def frame(self):
        return Config._frame
    
    @staticmethod
    def set_frame(frame: Frame):
        Config._frame = frame
