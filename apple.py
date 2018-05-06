import random
import pygame
from game_functions import GameFunctions


class Apple(GameFunctions):
    # Class responsible for food that snake can eat
    def __init__(self):
        super().__init__()

    def apple_draw(self):
        # Draw apple on the screen
        pygame.draw.rect(self.game_display, (255, 0, 0),
                         [self.apple_x, self.apple_y, self.block_size, self.block_size])

    def apple_random(self):
        # Randomize position of apple
        self.apple_x = round(random.randrange
                             (0, self.display_width - self.block_size) / 10.0) * 10.0
        self.apple_y = round(random.randrange
                             (0, self.display_height - self.block_size) / 10.0) * 10.0

    def apple_check(self, lead_x, lead_y):
        # Check if snake ate apple
        if lead_x == self.apple_x and lead_y == self.apple_y:
            self.snake_length += 1
            self.apple_random()
