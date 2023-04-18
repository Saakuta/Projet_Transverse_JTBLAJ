import pygame
from game import Game

# Set up the game window
screen_width = 800
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))

# Create the game object
game = Game(screen)

# Start the game loop
while True:
    game.handle_events()
    game.update()
    game.draw()
    pygame.display.update()
