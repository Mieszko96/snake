import pygame
from logic import Logic
from apple import Apple

def run_game():
    pygame.init()
    clock = pygame.time.Clock()
    logic = Logic()
    apple = Apple()
    FPS = 30
    apple.apple_random()
    while True:

        logic.event()
        logic.check_border()
        logic.update(apple.snake_length)
        apple.apple_check(logic.lead_x,logic.lead_y)
        apple.apple_draw()

        pygame.display.update()
        clock.tick(FPS)
run_game()