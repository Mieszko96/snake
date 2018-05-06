import pygame
from logic import Logic
from apple import Apple


# Main function
def run_game():
    pygame.init()
    clock = pygame.time.Clock()
    logic = Logic()
    apple = Apple()
    apple.apple_random()
    while True:
        logic.event()
        logic.update(apple.snake_length)
        logic.lose_conditions(apple.snake_length)
        apple.apple_check(logic.lead_x, logic.lead_y)
        apple.apple_draw()
        pygame.display.update()
        clock.tick(logic.fps)


run_game()
