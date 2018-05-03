import pygame, sys
from game_functions import GameFunctions
class Player ():
    """A class to store all settings for Snake."""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.pos_x=600
        self.pos_y=400
    def draw(self):
        self.screen.fill((self.bg_color))
        pygame.draw.rect(self.screen,(0, 0, 255),pygame.Rect(self.screen_width / 2,                                                             self.screen_height / 2, 30, 30))
        pygame.display.flip()
        GameFunctions.move(self.pos_x,self.pos_y)