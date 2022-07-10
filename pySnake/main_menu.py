from enum import Enum

import pygame
from pygame.locals import K_UP, K_DOWN, K_RETURN
from common.frame import Frame, Config
from common.other import BaseColor
from pySnake import game


class CycleIterator:
    def __init__(self, arr):
        self.array = arr
        self.iterator = 0
    
    def next(self):
        self.iterator += 1
        
        if self.iterator > (self.length - 1):
            self.iterator = 0
        
        return self.array[self.iterator]
    
    def prev(self):
        self.iterator -= 1
    
        if self.iterator < 0:
            self.iterator = len(self.array) - 1
    
        return self.array[self.iterator]

    @property
    def current(self):
        return self.array[self.iterator]
        
    @property
    def length(self):
        return len(self.array)


class Menu(Enum):
    NEW_GAME = 'New Game'
    OPTIONS = 'Options'
    EXIT = 'Exit'


class MainMenu(Frame):
    def __init__(self):
        super().__init__()
        
        self._menu = Menu
        self.cycle_iterator = CycleIterator([
            Menu.NEW_GAME,
            Menu.OPTIONS,
            Menu.EXIT,
        ])

    @property
    def active_menu_item(self):
        return self.cycle_iterator.current

    def check_events(self, event) -> None:
        """ Check keycode events """
        if event.key == K_UP:
            self.cycle_iterator.prev()
        elif event.key == K_DOWN:
            self.cycle_iterator.next()
        elif event.key == K_RETURN:
            self.on_enter()

    def on_enter(self):
        if self.active_menu_item == Menu.NEW_GAME:
            snake_game = game.SnakeGame()
            Config.set_frame(snake_game)
        elif self.active_menu_item == Menu.EXIT:
            self.close()

    def draw(self):
        color = BaseColor.BLACK

        self._window.fill(color)

        font = pygame.font.Font(None, 36)
        for index, item in enumerate(Menu):
            font_color = (255, 0, 0) if item == self.active_menu_item else (255, 255, 255)
            text = font.render(item.value, True, font_color)
            
            self._window.blit(text, (100, 50 + (index + 1) * 36))

    @property
    def timeout(self):
        return 0.1
        
    def game_over(self):
        pass
