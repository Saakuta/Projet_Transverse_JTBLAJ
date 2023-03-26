import pygame, os
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
keymap = {}

while True:
    event = pygame.event.wait()
    if event.type == KEYDOWN:
        keymap[event.scancode] = event.unicode
        print ('keydown %s pressed' % event.unicode)
        if (event.key == K_ESCAPE):
            os._exit(0)

    if event.type == KEYUP:
        print ('keyup %s pressed' % keymap[event.scancode])

 if movement == "Droite" and perso_x_deplacement != 0:
            perso.mvt_droite(perso_x, perso_y)
        elif movement == "Gauche" and perso_x_deplacement != 0:
            perso.mvt_gauche(perso_x, perso_y)
        if perso_x_deplacement == 0:
            perso.idle(perso_x, perso_y)