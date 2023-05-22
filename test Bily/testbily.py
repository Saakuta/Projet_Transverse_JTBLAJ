import pygame
from game import Game

pygame.init()

pygame.display.set_caption("Com fall Gall")
screen = pygame.display.set_mode((1920, 1080))

background = pygame.image.load('forest.jpg')

game = Game(screen)
running = True

while running:

    screen.blit(background, (0, 200))

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    if game.pressed.get(pygame.K_SPACE):
        game.player.jump()

    # Mettre à jour la position du joueur
    game.player.update(game.pressed)

    # Mettre à jour la fenêtre en fonction de la position du joueur
    screen.blit(background, (0, 200))
    game.player.draw(screen)

    # mettre à jour l'écran
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False