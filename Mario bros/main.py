import sys
import random

import pygame
from game import Game


# Set up the game window
screen_width = 800
screen_height = 750
screen = pygame.display.set_mode((screen_width,screen_height))

# Create the game object
game = Game(screen)


def main_menu():
    # Charger les images nécessaires
    logo_image = pygame.image.load("assets/LogoTitreGrand.png")
    background_image = pygame.image.load("assets/Fond_menu.png")
    play_button_image = pygame.image.load("assets/bouton_play.png")
    quit_button_image = pygame.image.load("assets/bouton_quit.png")

    # Afficher l'arrière-plan et le logo sur l'écran
    screen.blit(background_image, (screen_width, screen_height))
    screen.blit(logo_image, (screen_width / 2 - logo_image.get_width() / 2, 100))

    # Créer les rectangles pour les boutons "Play" et "Quit"
    play_button_rect = play_button_image.get_rect(center=(screen_width / 2, 400))
    quit_button_rect = quit_button_image.get_rect(center=(screen_width / 2, 500))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    # Action à effectuer lorsque le bouton "Play" est cliqué
                    print("Le bouton Play a été cliqué !")
                    start_game()  # Lancer la partie

                if quit_button_rect.collidepoint(event.pos):
                    # Action à effectuer lorsque le bouton "Quit" est cliqué
                    print("Le bouton Quit a été cliqué !")
                    pygame.quit()
                    sys.exit()

        # Dessiner les boutons sur l'écran
        screen.blit(play_button_image, play_button_rect)
        screen.blit(quit_button_image, quit_button_rect)

        pygame.display.update()

def start_game():

    player_rect = pygame.Rect(screen_width / 2 - 25, screen_height - 50, 50, 50)  # Rectangle du joueur

    fireball_image = pygame.image.load("assets/ball.png")
    fireball_rect = fireball_image.get_rect(bottomright=(screen_width, screen_height))  # Rectangle de la boule de feu
    fireball_speed_y = -8  # Vitesse verticale de la boule de feu

    jumping = False  # Indique si le personnage est en train de sauter
    jump_velocity = 10  # Vitesse initiale du saut
    gravity = 0.5  # Gravité pour la descente du personnage

    game_over = False
    while not game_over:
        game.handle_events()  # Gestion des événements (interactions utilisateur)
        game.update()  # Mise à jour de la logique du jeu
        game.draw()  # Dessin des éléments du jeu sur l'écran
        pygame.display.update()  # Mise à jour de l'affichage

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_rect.x -= 5
        if keys[pygame.K_RIGHT]:
            player_rect.x += 5

        if not jumping and keys[pygame.K_SPACE]:
            jumping = True
            jump_velocity = 10

        if jumping:
            player_rect.y -= jump_velocity
            jump_velocity -= gravity

            if player_rect.y >= screen_height - 50:
                jumping = False
                player_rect.y = screen_height - 50

        # Mettre à jour la position de la boule de feu selon la trajectoire parabolique
        fireball_speed_x = random.uniform(-25,0)  # Vitesse horizontale aléatoire entre -5 et 5
        fireball_acceleration_y = random.uniform(-0.35, 1.0)  # Accélération verticale aléatoire entre 0.1 et 1.0
        fireball_rect.x += fireball_speed_x
        fireball_speed_y += fireball_acceleration_y
        fireball_rect.y += fireball_speed_y

        # Vérifier si la boule de feu touche le joueur
        if fireball_rect.colliderect(player_rect):
            print("Le joueur a été touché par la boule de feu ! Le jeu est terminé.")
            game_over = True

        # Vérifier si la boule de feu est sortie de l'écran
        if fireball_rect.right < 0 or fireball_rect.top > screen_height:
            # La boule de feu est sortie de l'écran, réinitialiser sa position
            fireball_rect.bottomright = (screen_width, screen_height)
            fireball_speed_y = -10

        # Dessiner le joueur et la boule de feu sur l'écran
        pygame.draw.rect(screen, (255, 255, 255), player_rect)  # Dessiner le joueur sous forme d'un rectangle blanc
        screen.blit(fireball_image, fireball_rect)  # Dessiner la boule de feu

        pygame.display.update()

main_menu()