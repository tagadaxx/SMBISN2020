import pygame
from pygame.locals import *

screensize = (897, 672)
pygame.init()
fenetre = pygame.display.set_mode(screensize, RESIZABLE)

continuer = True
RUN, PAUSE = 0, 1
etat = RUN

fond = pygame.image.load("map.png").convert_alpha()
fond = pygame.transform.scale(fond, (10176,672))

while continuer:
    for event in pygame.event.get():

        if event.type == QUIT:
            continuer = False
            quit()

    fenetre.blit(fond, (0, 0))
    pygame.display.update()
    pygame.time.Clock().tick(60)