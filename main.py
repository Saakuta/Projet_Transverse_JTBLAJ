import pygame

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))


# Caption and Icon
pygame.display.set_caption("WIP")
icon = pygame.image.load('joystick.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('joystick.png')
playerX = 370
playerY = 480




# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.display.update()