import pygame
import sys
from player import Player

class Game:
    def __init__(self, screen):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = screen
        pygame.display.set_caption("Jumping in PyGame")
        self.player = Player(400, 630, self.screen.get_width()) # ajouter la largeur de l'écran ici
        self.background = pygame.image.load("assets/background.png")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()

                if event.key == pygame.K_LEFT:
                    self.player.start_move_left()

                if event.key == pygame.K_RIGHT:
                    self.player.start_move_right()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.stop_move_left()

                if event.key == pygame.K_RIGHT:
                    self.player.stop_move_right()

    def update(self):
        self.player.update()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.player.surface, self.player.rect)

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
