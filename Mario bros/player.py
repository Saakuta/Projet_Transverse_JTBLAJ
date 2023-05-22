import pygame
from animation import Animation


class Player(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position, screen_width, blocks_group):
        super().__init__()
        self.x_position = x_position
        self.y_position = y_position
        self.y_velocity = 0
        self.x_velocity = 0
        self.is_jumping = False
        self.is_on_block = False
        self.is_running = False
        self.current_frame = 0
        self.animation_timer = 0
        self.frame_delay = 200
        self.standing_surfaces = [
            pygame.transform.scale(pygame.image.load(f"assets/Idle/poulpily_idle{i}.png"), (48, 64))
            for i in range(1, 5)
        ]
        self.running_surfaces = [
            pygame.transform.scale(pygame.image.load(f"assets/Leg/poulpily_leg{i}.png"), (48, 64))
            for i in range(1, 6)
        ]
        self.running_animation = Animation(self.running_surfaces, frame_duration=100)  # Durée de chaque image : 100 ms

        self.jumping_surfaces = [
            pygame.transform.scale(pygame.image.load(f"assets/Jump/poulpily_jump{i}.png"), (48, 64))
            for i in range(1, 9)
        ]
        self.jumping_animation = Animation(self.jumping_surfaces, frame_duration=200)  # Durée de chaque image : 200 ms
        self.standing_animation = Animation(self.standing_surfaces, frame_duration=200)
        self.standing_surface = self.standing_surfaces[self.current_frame]
        self.rect = self.standing_surface.get_rect(center=(self.x_position, self.y_position))
        self.blocks_group = blocks_group
        self.y_gravity = 0.2
        self.jump_height = 10
        self.move_speed = 5
        self.run_speed = 8
        self.screen_width = screen_width

    def stop_move(self):
        self.x_velocity = 0
        self.is_running = False
        self.current_animation = self.standing_animation

    def update(self, dt):
        if self.is_jumping:
            self.y_position -= self.y_velocity
            self.y_velocity -= self.y_gravity
            if self.y_position >= 660:
                self.y_position = 660
                self.is_jumping = False
                self.y_velocity = 0
                self.current_frame = 0
                self.surface = self.standing_surfaces[self.current_frame]

        else:
            self.x_velocity = 0  # Réinitialiser la vitesse horizontale

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.x_velocity = -self.run_speed if self.is_running else -self.move_speed
                self.is_running = True
                self.current_animation = self.running_animation
            elif keys[pygame.K_RIGHT]:
                self.x_velocity = self.run_speed if self.is_running else self.move_speed
                self.is_running = True
                self.current_animation = self.running_animation
            else:
                self.is_running = False
                self.current_animation = self.standing_animation

            if pygame.sprite.spritecollide(self, self.blocks_group, False):
                self.is_on_block = True
            else:
                self.is_on_block = False

            if keys[pygame.K_SPACE] and (self.is_on_block or self.is_jumping):
                self.jump()

        self.animation_timer += dt  # Temps écoulé depuis le dernier appel à update()
        if self.animation_timer >= self.frame_delay:
            self.animation_timer = 0  # Réinitialiser le timer
            self.current_frame = (self.current_frame + 1) % len(self.standing_surfaces)  # Passage à l'image suivante
        self.surface = self.standing_surfaces[self.current_frame]

        self.x_position += self.x_velocity
        self.y_position -= self.y_velocity
        self.y_velocity -= self.y_gravity

        if self.x_position < 0:
            self.x_position = 0
        elif self.x_position > self.screen_width - self.rect.width:
            self.x_position = self.screen_width - self.rect.width

        if self.y_position >= 660:
            self.y_position = 660
            self.is_jumping = False
            self.y_velocity = 0
            self.current_frame = 0
            self.surface = self.standing_surfaces[self.current_frame]

        if self.is_jumping:
            self.current_animation = self.jumping_animation
        elif self.is_running:
            self.current_animation = self.running_animation
        else:
            self.current_animation = self.standing_animation

        self.current_animation.update(dt)
        self.surface = self.current_animation.get_current_frame()

        self.rect = self.surface.get_rect(center=(self.x_position, self.y_position))

        self.check_platform_collision()

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.y_velocity = self.jump_height
            self.surface = self.jumping_surfaces[0]  # Utiliser la première image de l'animation de saut

    def start_move_left(self):
        self.x_velocity = -self.run_speed
        self.is_running = True
        self.current_animation = self.running_animation

    def stop_move_left(self):
        if self.x_velocity < 0:
            self.x_velocity = 0
            if not self.is_running:
                self.current_animation = self.standing_animation

    def start_move_right(self):
        self.x_velocity = self.run_speed
        self.is_running = True
        self.current_animation = self.running_animation

    def stop_move_right(self):
        if self.x_velocity > 0:
            self.x_velocity = 0
            if not self.is_running:
                self.current_animation = self.standing_animation

    def check_platform_collision(self):
        collision_blocks = pygame.sprite.spritecollide(self, self.blocks_group, False)
        if collision_blocks:
            block = collision_blocks[0]  # Obtenir le premier bloc en collision
            if self.y_velocity > 0:  # Vérifier si le personnage est en train de tomber
                self.rect.bottom = block.rect.top
                self.is_jumping = False
                self.y_velocity = 0
                self.surface = self.standing_surface
                self.is_on_block = True
            elif self.y_velocity < 0:  # Vérifier si le personnage est en train de sauter vers le haut
                self.rect.top = block.rect.bottom
                self.y_velocity = 0
                self.is_jumping = False
                self.surface = self.standing_surface
            else:  # Vérifier si le personnage est en contact avec un bloc sur les côtés
                if self.rect.right > block.rect.left and self.x_velocity > 0:
                    self.rect.right = block.rect.left
                    self.x_velocity = 0
                elif self.rect.left < block.rect.right and self.x_velocity < 0:
                    self.rect.left = block.rect.right
                    self.x_velocity = 0
            self.is_on_block = True
        else:
            self.is_on_block = False

    def stop_jump(self):
        self.y_velocity = 0
        self.is_jumping = False
        self.surface = self.standing_surface