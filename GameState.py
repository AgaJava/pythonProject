import random
from Position import Position
from Direction import Direction

INITIAL_SNAKE = [Position(1, 2), Position(2, 2), Position(3, 2)]
INITIAL_DIRECTION = Direction.RIGHT


class GameState:
    def __init__(self, snake, direction, food, field_size):
        self.snake = snake
        self.direction = direction
        self.food = food
        self.field_size = field_size

    def set_initial_position(self):
        self.snake = INITIAL_SNAKE[:]
        self.direction = INITIAL_DIRECTION
        self.set_random_food_position()

    def next_head_position(self, direction):
        pos = self.snake[-1]
        if direction == Direction.UP:
            return Position(pos.x, (pos.y - 1) % self.field_size)
        elif direction == Direction.DOWN:
            return Position(pos.x, (pos.y + 1) % self.field_size)
        elif direction == Direction.RIGHT:
            return Position((pos.x + 1) % self.field_size, pos.y)
        elif direction == Direction.LEFT:
            return Position((pos.x - 1) % self.field_size, pos.y)

    def set_random_food_position(self):
        self.food = Position(
            random.randint(0, self.field_size -1),
            random.randint(0, self.field_size -1)
        )
        if self.food in self.snake:
            self.set_random_food_position()

    def step(self):
        new_head_position = self.next_head_position(self.direction)

        if new_head_position in self.snake:
            self.set_initial_position()
            return
        self.snake.append(new_head_position)

        if new_head_position == self.food:
            self.set_random_food_position()
        else:
            self.snake = self.snake[1:]

    def turn(self, direction):
        if self.can_turn(direction):
            self.direction = direction

    def can_turn(self, direction):
        new_head_position = self.next_head_position(direction)
        return new_head_position != self.snake[-2]











