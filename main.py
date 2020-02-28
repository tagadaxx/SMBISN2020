import pygame
from pygame.locals import *

screensize = (1280, 720)
pygame.init()
fenetre = pygame.display.set_mode(screensize, RESIZABLE)

continuer = True
RUN, PAUSE = 0, 1
etat = RUN

fond = pygame.image.load("overworld_bg.png").convert_alpha()

while continuer:
    for event in pygame.event.get():

        if event.type == QUIT:
            continuer = False
            quit()

    fenetre.blit(fond, (0, 0))