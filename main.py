import pygame
from pygame.locals import *

screensize = (1280, 720)
pygame.init()
fenetre = pygame.display.set_mode(screensize, RESIZABLE)

continuer = True
RUN, PAUSE = 0, 1
etat = RUN

fond = pygame.image.load("cheems.jpg").convert_alpha()

while continuer:
    for event in pygame.event.get():

        if event.type == QUIT:
            continuer = False
            quit()
    fond = pygame.image.load("cheems.jpg").convert_alpha()
    fenetre.blit(fond, (10, 10))