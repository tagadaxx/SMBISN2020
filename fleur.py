import pygame

class Fleurfeu :
    def __init__(self, 109,4):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("FireFlower.gif").convert_alpha
        self.rect = self.image.getrect
        self.rect.center = center
