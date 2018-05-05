import pygame,sys
from game_functions import GameFunctions
game=GameFunctions()
pygame.init()
clock = pygame.time.Clock()

block_size = 10
FPS = 30
def run_game():
    lead_x = game.display_width / 20
    lead_y = game.display_height / 20

    lead_x_change = 0
    lead_y_change = 0

    snake_list = []
    snake_length = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and lead_x_change <= 0:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT and lead_x_change >= 0:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP and lead_y_change <= 0:
                    lead_x_change = 0
                    lead_y_change = -block_size
                elif event.key == pygame.K_DOWN and lead_y_change >= 0:
                    lead_x_change = 0
                    lead_y_change = block_size
        # End the game when users move outside of screen dimensions
        if not 0 < lead_x <= game.display_width or not 0 < lead_y <= game.display_height:
            sys.exit()
        # Apply changes to position, this creates motion
        lead_x += lead_x_change
        lead_y += lead_y_change
        # Paint the background
        game.gameDisplay.fill((0, 0, 0))
        # Create snake segment as list of x and y coordinates, add to end of snake list
        snake_segment = [lead_x, lead_y]
        print (snake_segment)

        snake_list.append(snake_segment)

        # When the length of the snake exceeds the limit defined, erase the new segment
        if len(snake_list) > snake_length:
            snake_list.pop(0)

        game.snake(block_size, snake_list)
        pygame.display.update()
        clock.tick(FPS)

run_game()