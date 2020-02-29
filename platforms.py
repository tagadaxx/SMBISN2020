import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,imgw,imgh,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img).convert_alpha()
        self.imgw = imgw
        self.imgh = imgh
        self.image = pygame.transform.scale(self.image, (self.imgw, self.imgh))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    def rect(self) :
        return self.rect
