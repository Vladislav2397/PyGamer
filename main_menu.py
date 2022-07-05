from enum import Enum

import pygame
from pygame.surface import Surface
from common.base_game import BaseGame
from common.other import MyColor


class Menu(Enum):
    NEW_GAME = 'New Game'
    OPTIONS = 'Options'
    EXIT = 'Exit'


class MainMenu(BaseGame):
    def __init__(self):
        super().__init__()
        
        self._menu = Menu
        self._active_menu_item = self._menu.NEW_GAME
    
    def run(self):
        super().run()

    def draw(self, window: Surface):
        color = MyColor.BLACK

        window.fill(color)

        font = pygame.font.Font(None, 36)
        for index, item in enumerate(Menu):
            text = font.render(item.value, True, (255, 255, 255))
            
            window.blit(text, (100, 50 + (index + 1) * 36))
        
    def game_over(self):
        pass
