import pygame
from player import Player

#création de la class GAME pour représenter le jeu
class Game: 

    def __init__(self):
        #generer le joueur
        self.player = Player()
        
        self.pressed = {}