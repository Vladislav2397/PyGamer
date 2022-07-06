from pygame.sprite import Group

from common.base_game import BaseGame
from common.other import MyColor

from pySnake.eat import Eat
from pySnake.snake import Snake


class SnakeGame(BaseGame):
    def __init__(self):
        super().__init__()
        
        self.snake = Snake(
            color=MyColor.GREEN,
        )
        self.eat = Eat(pos=[40, 20], color=MyColor.RED)
        self._all_groups = Group(*self.snake, self.eat)

    def check_events(self, event):
        pass
    
    def update(self):
        pass
    
    def draw(self):
        pass
    
    def run(self):
        pass

    def game_over(self):
        pass
