import pygame

class perso(pygame.sprite.Sprite):

    def __init__(self, image, x, y, imgw, imgh):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.imw = imgw
        self.img = imgh

    def vie(mavie, x=50, y=50):
        mavie = 5
        if perdu:
            mavie = mavie-1
        print(mavie)
