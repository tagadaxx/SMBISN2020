import pygame

class Fleurfeu :
    def __init__(self, (x)109,(y)4):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("FireFlower.gif").convert_alpha
        self.rect = self.image.get.rect
        self.rect.center = center
