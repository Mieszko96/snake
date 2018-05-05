import pygame,sys
from game_functions import GameFunctions

class Logic(GameFunctions):
    def __init__(self):
        super().__init__()
        self.lead_x_change = 0
        self.lead_y_change = 0
        self.snake_list = []

    def event(self):
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
    def check_border(self):
        if not 0 < self.lead_x <= self.display_width or not\
                0 < self.lead_y <= self.display_height:
            sys.exit()
    def update(self,snake_length):
        print (snake_length)
        self.lead_x += self.lead_x_change
        self.lead_y += self.lead_y_change
        snake_segment = [self.lead_x, self.lead_y]
        self.snake_list.append(snake_segment)
        if len(self.snake_list) > snake_length:
            self.snake_list.pop(0)
        self.gameDisplay.fill((0, 0, 0))
        self.snake(self.block_size, self.snake_list)

