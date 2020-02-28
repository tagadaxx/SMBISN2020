import pygame
from Perso import perso
from pygame.locals import *

screensize = (897, 672)
pygame.init()
fenetre = pygame.display.set_mode(screensize, RESIZABLE)

continuer = True
RUN, PAUSE = 0, 1
etat = RUN

fond = pygame.image.load("map.png").convert_alpha()
fond = pygame.transform.scale(fond, (10176,672))

pygame.key.set_repeat(100, 25)
mario = perso("SuperMarioWalk3.gif")

while continuer:
    for event in pygame.event.get():

        if event.type == QUIT:
            continuer = False
            quit()
        if event.type == KEYDOWN :
            if event.key == K_UP:
                mario.y += 10
            if event.key == K_DOWN:
                mario.y += 10
            if event.key == K_LEFT:
                mario.x += -10
            if event.key == K_RIGHT:
                mario.x += 10



    fenetre.blit(fond, (0, 0))
    fenetre.blit(mario.image, (64,512))
    pygame.display.update()
    pygame.time.Clock().tick(60)