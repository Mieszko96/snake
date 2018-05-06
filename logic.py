import pygame
import sys
from game_functions import GameFunctions


class Logic(GameFunctions):
    # Class responsible for logic of snake
    def __init__(self):
        super().__init__()
        self.lead_x_change = 0
        self.lead_y_change = 0
        self.snake_list = []

    def event(self):
        # Method that check inputs from player
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.lead_x_change <= 0:
                    self.lead_x_change = -self.block_size
                    self.lead_y_change = 0
                elif event.key == pygame.K_RIGHT and self.lead_x_change >= 0:
                    self.lead_x_change = self.block_size
                    self.lead_y_change = 0
                elif event.key == pygame.K_UP and self.lead_y_change <= 0:
                    self.lead_x_change = 0
                    self.lead_y_change = -self.block_size
                elif event.key == pygame.K_DOWN and self.lead_y_change >= 0:
                    self.lead_x_change = 0
                    self.lead_y_change = self.block_size

    def lose_conditions(self, snake_length):
        # Method that checking lose_condition

        if not 0 < self.lead_x <= self.display_width or not\
                0 < self.lead_y <= self.display_height:
            print("You got {} points".format(snake_length))
            sys.exit()
        snake_head = [self.lead_x, self.lead_y]
        for each in self.snake_list[:-1]:
            if each == snake_head:
                print("You got {} points".format(snake_length))
                sys.exit()

    def update(self, snake_length):
        # Method to update position of the body
        self.lead_x += self.lead_x_change
        self.lead_y += self.lead_y_change
        snake_head = [self.lead_x, self.lead_y]
        self.snake_list.append(snake_head)
        if len(self.snake_list) > snake_length:
            self.snake_list.pop(0)
        self.game_display.fill((0, 0, 0))
        self.draw_snake(self.block_size, self.snake_list)
        