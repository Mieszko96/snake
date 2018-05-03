import pygame,sys
#from pygame.math import Vector2
#from player import Player
class GameFunctions():
    def __init__(self):
        pass
    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            print("dupa")
        if pressed[pygame.K_s]:
            print("dupa")
        if pressed[pygame.K_a]:
            print("dupa")
        if pressed[pygame.K_d]:
            print("dupa")



    def move(self, pos_x,pos_y):

        print(pos_x)
        print (pos_y)
