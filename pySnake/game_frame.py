from time import time
from pygame.locals import (
    KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_ESCAPE
)
from pygame.time import Clock
from pygame.surface import Surface
from pygame.sprite import collide_rect
from pySnake.snake import Snake
from pySnake.eat import Eat
from common.tools import MyColor, Window, AllSprites

from common.config import (
    LEFT, RIGHT, UP, DOWN, SPEED
)


class SnakeGameFrame:

    def __init__(self, application) -> None:
        """ Initialize of 'GAME' object """

        self._app = application
        self._window = Surface(Window())
        self._width, self._height = self._window.get_size()
        self._is_play = True
        self._timer = time()
        self._time = Clock()

        self.snake = Snake(
            color=MyColor.GREEN,
            window_size=(self._width, self._height)
        )
        self.eat = Eat(pos=[40, 20], color=MyColor.RED)
        self._all_groups = AllSprites(self.snake, self.eat)

    def _check_colliderect(self):
        """ Check has collide rect """

        hit = collide_rect(self.snake.head, self.eat)
        if hit:
            self.snake.upgrade()
            self.eat.upgrade(self.snake.get_positions)

    def loop(self, events):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pass
                elif event.key == K_LEFT:
                    self.snake.turn(LEFT)
                elif event.key == K_RIGHT:
                    self.snake.turn(RIGHT)
                elif event.key == K_UP:
                    self.snake.turn(UP)
                elif event.key == K_DOWN:
                    self.snake.turn(DOWN)

        self._all_groups.add([*self.snake.body, self.eat])
        if self.is_time:
            self.snake.move()
            self._check_colliderect()
            self.eat.update()
            self.snake.update()
            self._window.fill(MyColor.BLACK)
            self._all_groups.draw(self._window)
            self._app.window.blit(self._window, (0, 0))

    def set_as_main_surface(self):
        self._app.set_surface(self)

    @property
    def is_time(self) -> bool:
        """ It's property return boolean if is timeout """

        if self._timer < time():
            self._timer = time() + SPEED
            return True
        return False
