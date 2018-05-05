import pygame,sys
class GameFunctions():

    def __init__(self):
        self.display_width = 800
        self.display_height = 600
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('SEC Snake Tutorial')
    def snake(self,block_size,snake_list):
        # Iterate through each segment in the list
        for segment in snake_list:
            # Segments consist of x and y coordinates
            lead_x, lead_y = segment
            # Draw each segment at its respective location
            pygame.draw.rect(self.gameDisplay, (0, 150, 0),
                             [lead_x, lead_y, block_size, block_size])


