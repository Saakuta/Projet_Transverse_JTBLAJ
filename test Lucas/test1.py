import pygame
from game import Game
pygame.init()


#Création de la fenêtre

pygame.display.set_caption("Titre du jeu") #Nom du canvas
screen = pygame.display.set_mode((1280,720)) #Résolution

#charger image 
background = pygame.image.load('test Lucas/images/Background.jpg')

#charger le jeu
game = Game()


#boucle pour maintenir le canvas ouvert
running = True

while running:

    #applique le backgroud dans le canvas
    screen.blit(background, (0, -100))

    #applique l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    #Mettre à jour le canvas
    pygame.display.flip()

    #si fermeture canvas
    for event in pygame.event.get(): #boucle pour tous les events 

        if event.type == pygame.QUIT:
            running = False
            pygame.quit() #Ferme le canvas
