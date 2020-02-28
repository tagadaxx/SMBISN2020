import pygame

class Fleurfeu :
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("FireFlower.gif").convert_alpha
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = center
