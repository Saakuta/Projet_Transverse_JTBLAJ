import pygame

class Player:
    def __init__(self, x_position, y_position, screen_width):
        self.x_position = x_position
        self.y_position = y_position
        self.y_velocity = 0
        self.x_velocity = 0
        self.is_jumping = False
        self.jumping_surface = pygame.transform.scale(pygame.image.load("assets/mario_jumping.png"), (48, 64))
        self.standing_surface = pygame.transform.scale(pygame.image.load("assets/mario_standing.png"), (48, 64))
        self.surface = self.standing_surface
        self.rect = self.surface.get_rect(center=(self.x_position, self.y_position))
        self.jumping = False
        self.y_gravity = 0.3
        self.jump_height = 10
        self.move_speed = 5
        self.screen_width = screen_width

    def update(self):
        if self.is_jumping:
            self.y_position -= self.y_velocity
            self.y_velocity -= self.y_gravity
            if self.y_position >= 660:
                self.y_position = 660
                self.is_jumping = False
                self.y_velocity = 0
                self.surface = self.standing_surface
        else:
            self.surface = self.standing_surface

        self.rect = self.surface.get_rect(center=(self.x_position, self.y_position))
        self.x_position += self.x_velocity
        if self.x_position < 0:
            self.x_position = 0
        elif self.x_position > self.screen_width - self.rect.width:
            self.x_position = self.screen_width - self.rect.width
        if self.y_velocity > 0:
            self.surface = self.jumping_surface
        else:
            self.surface = self.standing_surface
        self.y_position -= self.y_velocity
        self.y_velocity -= self.y_gravity
        if self.y_position >= 660:
            self.y_position = 660
            self.is_jumping = False
            self.y_velocity = 0
            self.surface = self.standing_surface
        if self.is_jumping:
            self.surface = self.jumping_surface
        self.rect = self.surface.get_rect(center=(self.x_position, self.y_position))

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.y_velocity = self.jump_height
            self.surface = self.jumping_surface

    def start_move_left(self):
        self.x_velocity = -self.move_speed

    def stop_move_left(self):
        if self.x_velocity < 0:
            self.x_velocity = 0

    def start_move_right(self):
        self.x_velocity = self.move_speed

    def stop_move_right(self):
        if self.x_velocity > 0:
            self.x_velocity = 0
