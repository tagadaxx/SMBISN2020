import pygame

class Platform(pygame.sprite.Sprite):
# x location, y location, img width, img height, img file    
    def __init__(self,x,y,imgw,imgh,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img).convert_alpha()
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x