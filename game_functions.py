import pygame
class GameFunctions():

    def __init__(self):
        self.display_width = 800
        self.display_height = 600
        self.snake_length = 1
        self.lead_x = self.display_width / 2
        self.lead_y = self.display_height / 2
        self.block_size = 10

        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Snake Game')
    def snake(self,block_size,snake_list):

        for segment in snake_list:
            lead_x, lead_y = segment
            pygame.draw.rect(self.gameDisplay, (0, 150, 0),
                             [lead_x, lead_y, block_size, block_size])


