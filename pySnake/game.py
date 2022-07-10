from pygame.sprite import Group
from pygame.locals import K_ESCAPE
from pygame.sprite import collide_rect
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN

from common.config import (
    UP, DOWN, LEFT, RIGHT,
)
from common.frame import Frame, Config
from common.other import BaseColor
import pySnake

from pySnake.eat import Eat
from pySnake.snake import Snake


class SnakeGame(Frame):
    def __init__(self):
        super().__init__()
        
        self.snake = Snake(
            color=BaseColor.GREEN,
        )
        self.eat = Eat(pos=[40, 20], color=BaseColor.RED)
        # self._all_groups = Group(*self.snake, self.eat)

    def check_events(self, event):
        if event.key == K_ESCAPE:
            menu = pySnake.main_menu.MainMenu()
            Config.set_frame(menu)
        if event.key == K_LEFT:
            self.snake.turn(LEFT)
        elif event.key == K_RIGHT:
            self.snake.turn(RIGHT)
        elif event.key == K_UP:
            self.snake.turn(UP)
        elif event.key == K_DOWN:
            self.snake.turn(DOWN)

    def update(self):
        pass
    
    @property
    def all_groups(self):
        return Group(self.eat, *self.snake)
    
    def draw(self):
        self.snake.move()
        self._check_collide_rect()
        self.eat.update()
        self.snake.update()
        self._window.fill(BaseColor.BLACK)
        self.all_groups.draw(self._window)
    
    def _check_collide_rect(self):
        hit = collide_rect(self.snake.head, self.eat)
        if hit:
            self.eat.upgrade(self.snake.get_positions)
            self.snake.upgrade()

    def run(self):
        pass

    def game_over(self):
        pass
