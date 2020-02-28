import pygame


class perso:
    def __init__(self, image, x, y):
        self.image = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y


    def vie(mavie, x=50, y=50):
        mavie = 5
        if perdu:
            mavie = mavie-1
        print(mavie)

