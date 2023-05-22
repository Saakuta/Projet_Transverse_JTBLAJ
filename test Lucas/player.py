import pygame

#Création de la class joueur
class Player(pygame.sprite.Sprite): #0n attribut le superclass sprite pr pvr mettre une image, bouger... avec le joueur 

    def __init__(self):
        super().__init__()
        self.health = 1 #Il a une vie
        self.maxhealth = 1
        self.velocity = 2 #vitesse de déplacement
        self.image = pygame.image.load('test Lucas/images/jett.jpg').convert_alpha() #image du joueur 
        self.rect = self.image.get_rect() #dimension du joueur 
        self.rect.x = 400
        self.rect.y = 500

    
    def move_up(self):
        self.rect.y -= self.velocity

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity