import pygame
from player import Player
from game_functions import GameFunctions
def run_game():
    pygame.init()
    player=Player()
    game=GameFunctions()
    pygame.display.set_caption("Snake")
    while True:
        player.draw()
        game.input()
        game.move()

run_game()