import pygame

#Création de la class joueur
class Player(pygame.sprite.Sprite): #0n attribut le superclass sprite pr pvr mettre une image, bouger... avec le joueur 

    def __init__(self):
        super().__init__()
        self.health = 1 #Il a une vie 
        self.maxhealth = 1
        self.velocity = 10
        self.image = pygame.image.load('test Lucas/images/jett.jpg') #image du joueur 
        self.rect = self.image.get_rect() #dimension du joueur 
        self.rect.x = 400
        self.rect.y = 500