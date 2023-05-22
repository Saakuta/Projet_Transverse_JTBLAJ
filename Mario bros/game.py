import pygame
import sys
from player import Player


class Game:
    def __init__(self, screen):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = screen
        pygame.display.set_caption("Bibi bebou <3")
        self.background = pygame.image.load("assets/background.png")
        self.clock = pygame.time.Clock()

        self.player = Player(400, 630, self.screen.get_width())
        self.is_on_block = False

        self.start_time = pygame.time.get_ticks()  # Temps de début du jeu en millisecondes
        self.timer_font = pygame.font.Font(None, 36)  # Police d'écriture pour le timer

    def update(self):
        dt = self.clock.tick(60)  # Obtenir le temps écoulé depuis la dernière mise à jour (en millisecondes)
        self.player.update(dt)  # Passer dt à la méthode update() du joueur

        # Mettre à jour le canvas
        self.draw()
        pygame.display.flip()

        # Vérifier le temps écoulé
        elapsed_time = pygame.time.get_ticks() - self.start_time
        if elapsed_time >= 60000:  # 60 secondes (ajustez la valeur selon vos besoins)
            self.game_over()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.player.surface, self.player.get_hitbox())

        # Afficher le temps écoulé
        elapsed_time = pygame.time.get_ticks() - self.start_time
        seconds = int(elapsed_time / 1000)  # Conversion en secondes
        timer_text = self.timer_font.render("Temps: {}s".format(seconds), True, (255, 255, 255))
        self.screen.blit(timer_text, (10, 10))


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

    def game_over(self):
        print("Temps écoulé. Game Over!")
        pygame.quit()
        sys.exit()

