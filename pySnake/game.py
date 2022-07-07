from pygame.sprite import Group
from pygame.locals import K_ESCAPE

from common.frame import Frame, Config
from common.other import MyColor
import pySnake

from pySnake.eat import Eat
from pySnake.snake import Snake


class SnakeGame(Frame):
    def __init__(self):
        super().__init__()
        
        self.snake = Snake(
            color=MyColor.GREEN,
        )
        self.eat = Eat(pos=[40, 20], color=MyColor.RED)
        self._all_groups = Group(*self.snake, self.eat)

    def check_events(self, event):
        if event.key == K_ESCAPE:
            menu = pySnake.main_menu.MainMenu()
            Config.set_frame(menu)
    
    def update(self):
        pass
    
    def draw(self):
        pass
    
    def run(self):
        pass

    def game_over(self):
        pass
