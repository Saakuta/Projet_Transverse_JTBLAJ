import pygame
from game import Game
import math

# Set up the game window
screen_width = 800
screen_height = 750
screen = pygame.display.set_mode((screen_height,screen_height))

# Create the game object
game = Game(screen)

# Start the game loop


while True:



    game.handle_events()  # Gestion des événements (interactions utilisateur)
    game.update()  # Mise à jour de la logique du jeu
    game.check_collision()  # Vérifier les collisions entre le joueur et les blocs
    game.draw()  # Dessin des éléments du jeu sur l'écran
    pygame.display.update()  # Mise à jour de l'afficha ge