import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, screen=None):
        super().__init__()
        self.screen = screen
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.jump_velocity = -400  # Ajustez cette valeur pour contrôler la hauteur du saut
        self.jump_height = 400
        self.gravity = 1
        self.image = pygame.image.load('minou.png')
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 600
        self.ground_y = self.rect.y
        self.is_jumping = False
        self.jump_start_y = self.rect.y
        self.jump_peak_y = None
        self.jump_end_y = None
        self.jump_start_time = None
        self.jump_duration = None
        self.vertical_velocity = 0

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_start_y = self.rect.y
            self.jump_peak_y = self.jump_start_y - self.jump_height
            self.jump_end_y = self.ground_y
            self.jump_start_time = pygame.time.get_ticks()
            self.jump_duration = 0

    def update(self, pressed):
        if self.is_jumping:
            self.jump_duration = pygame.time.get_ticks() - self.jump_start_time
            if self.jump_duration >= 2 * abs(self.jump_velocity) / self.gravity:
                self.is_jumping = False
                self.rect.y = self.ground_y
            else:
                t = self.jump_duration / 1000  # convertir en secondes
                a = self.gravity
                v0 = self.jump_velocity
                y0 = self.jump_start_y
                y = -0.5 * a * t ** 2 + v0 * t + y0  # calculer la position actuelle du joueur
                self.rect.y = y
        if self.x_position < 0:
            self.x_position = 0
        elif self.x_position > self.screen_width - self.rect.width:
            self.x_position = self.screen_width - self.rect.width
        # empêcher le joueur de sortir de l'écran
        if self.x_position < 0:
            self.x_position = 0
        elif self.x_position > self.screen_width - self.rect.width:
            self.x_position = self.screen_width - self.rect.width
        if self.rect.bottom > self.screen.get_height():
            self.rect.bottom = self.screen.get_height()

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > self.screen.get_width():
            self.rect.right = self.screen.get_width()

        if self.health <= 0:
            print("Game Over")

    def draw(self, screen):
        screen.blit(self.image, self.rect)
