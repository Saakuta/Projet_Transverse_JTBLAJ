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
playerImg = pygame.image.load('8 ball.png')
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX, playerY))

perso_x_deplacement = 0

perso = player()


# Game loop
running = True
movement = False
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




        # if keystroke is pressed check wether it's right or lefteee
        if event.type == pygame.KEYDOWN:
            print(event.unicode)
            if event.type == pygame.K_q:
                playerX -= 5
                print("Left arrow is pressed")
            if event.type == pygame.K_d:
                playerY += 5
                print("Right arrow is pressed")
            player()
            pygame.display.update()
        if event.type == pygame.KEYUP:
            if event.type == pygame.K_q or event.type == pygame.K_d:
                print("Keystroke has been released")
        player()
        pygame.display.update()

    player()
    pygame.display.update()