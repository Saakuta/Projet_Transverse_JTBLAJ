import pygame
from player import Player


class Game:

    def __init__(self, screen):
        self.screen = screen
        self.player = Player(screen)  # passer screen ici
        self.pressed = {}

    def run(self):
        self.player.update(self.pressed)
        self.player.draw(self.screen)
