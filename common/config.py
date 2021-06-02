import pygame

BLOCK_SIZE = 20
BLOCK_SIZE_TUPLE = (BLOCK_SIZE, BLOCK_SIZE)
WINDOW_SIZE = (
    BLOCK_SIZE * 40,
    BLOCK_SIZE * 35
)

MAIN_WINDOW_SURFACE = pygame.display.set_mode(WINDOW_SIZE)

FPS = 30
TIMEOUT = 3
SPEED = 0.5 - (0.1 * TIMEOUT)

LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'
CLOSE = 'close'
