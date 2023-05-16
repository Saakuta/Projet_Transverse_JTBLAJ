import pygame
from game import Game
pygame.init()


#Création de la fenêtre

pygame.display.set_caption("C moi wsh") #Nom du canvas

icon = pygame.image.load('images\Edamura.jpg') #icone de la fenêtre
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((1280,720)) #Résolution

#charger image 
background = pygame.image.load('test lucas/images/Background.jpg')

#charger le jeu
game = Game()


#boucle pour maintenir le canvas ouvert
running = True


while running:

    #applique le backgroud dans le canvas
    screen.blit(background, (0, -100))

    #applique l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    #vérifier si le joueur souhaite aller à gauche ou à droite, haut et bas
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < screen.get_width() - game.player.rect.width:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
    elif game.pressed.get(pygame.K_UP) and game.player.rect.y > 0:
        game.player.move_up()
    elif game.pressed.get(pygame.K_DOWN) and game.player.rect.y < screen.get_height() - game.player.rect.height:
        game.player.move_down()



    #Mettre à jour le canvas
    pygame.display.flip()

    #si fermeture canvas
    for event in pygame.event.get(): #boucle pour tous les events 

        if event.type == pygame.QUIT: #evenement fermeture 
            running = False
            pygame.quit() #Ferme le canvas

        
        elif event.type == pygame.KEYDOWN: #evenement de detection de touche
            game.pressed[event.key] = True #on ajoute la touche dans le dictionnaire

            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit() #Ferme le canvas
        
        elif event.type == pygame.KEYUP:#touche non detectée
            game.pressed[event.key] = False
