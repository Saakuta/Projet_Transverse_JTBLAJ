import pygame
import math
from player import Player

#création de la class GAME pour représenter le jeu
class Game: 

    def __init__(self):
        #generer le joueur
        self.player = Player()
        self.pressed = {}

        #definir si notre jeu a commencé
        self.is_playing = False

        #jeu en pause
        self.is_pause = False

        self.debut_timer = 0






    def update(self,screen):
            # applique l'image du joueur
            screen.blit(self.player.image, self.player.rect)

            # vérifier si le joueur souhaite aller à gauche ou à droite, haut et bas
            if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < screen.get_width() - self.player.rect.width:
                self.player.move_right()


            elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
                self.player.move_left()

            elif self.pressed.get(pygame.K_UP) and self.player.rect.y > 0:
                self.player.move_up()

            elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y < screen.get_height() - self.player.rect.height:
                self.player.move_down()


            # Mettre à jour le canvas
            pygame.display.flip()



            #timer
            if self.is_playing :
                secondes = (self.debut_timer + pygame.time.get_ticks()//1000)

            self.creer_message('grande','{}'.format(secondes),[math.ceil(screen.get_width()/27),math.ceil(screen.get_width()/30),20,20],(255,255,255),screen)

            # si fermeture canvas
            for event in pygame.event.get():  # boucle pour tous les events

                if event.type == pygame.QUIT:  # evenement fermeture

                    running = False
                    pygame.quit()  # Ferme le canvas


                elif event.type == pygame.KEYDOWN:  # evenement de detection de touche
                    self.pressed[event.key] = True  # on ajoute la touche dans le dictionnaire

                    if event.key == pygame.K_ESCAPE:
                        self.is_playing = False
                        self.is_pause = True



                        ##running = False
                        ##pygame.quit()  # Ferme le canvas

                elif event.type == pygame.KEYUP:  # touche non detectée
                    self.pressed[event.key] = False
    def creer_message(self, font, message, message_rectangle, couleur,screen):
            if font == 'petite':
                font = pygame.font.SysFont('latos',20,False)
            elif font == 'moyennne':
                font = pygame.font.SysFont('latos', 30, False)
            elif font == 'grande':
                font = pygame.font.SysFont('latos', 40, True)
            message = font.render(message,True,couleur)

            screen.blit(message, message_rectangle)










