from common.block import Block
from common.other import BaseColor
from common.position import Position
from common.config import MoveDirection


def next_block_position(block: Block, direction: MoveDirection):
    position = None
    
    if direction == MoveDirection.UP:
        position = [block.position.x, block.position.y - block.size]
    elif direction == MoveDirection.LEFT:
        position = [block.position.x - block.size, block.position.y]
    elif direction == MoveDirection.DOWN:
        position = [block.position.x, block.position.y + block.size]
    else:
        position = [block.position.x + block.size, block.position.y]
    
    return Position(*position)


def colored_block_factory(color=BaseColor.GREEN):
    def block_factory(*pos):
        return Block(pos=Position(*pos), color=color)
    
    return block_factory
