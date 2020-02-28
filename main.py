import pygame
from Perso import perso
from pygame.locals import *

screensize = (897, 672)
pygame.init()
fenetre = pygame.display.set_mode(screensize, RESIZABLE)
jump, xaya = 0, -3
continuer = True
RUN, PAUSE = 0, 1
etat = RUN
initjump = 0
fond = pygame.image.load("map.png").convert_alpha()
fond = pygame.transform.scale(fond, (10176,672))


pygame.key.set_repeat(100, 25)
mario = perso("SuperMarioWalk3.gif", 64, 512)
MarioState = 0
while continuer:

    for event in pygame.event.get():

        if event.type == QUIT:
            continuer = False
            quit()
        if event.type == KEYDOWN :
            if event.key == K_UP and jump == 0:
                jump = 1
            if event.key == K_DOWN and MarioState == 1:
                mario = perso("mariocrouch.gif", mario.x, mario.y)
            if event.key == K_LEFT:
                mario.x += -10
            if event.key == K_RIGHT:
                mario.x += 10
        if event.type == KEYUP :
            if event.key == K_DOWN :
                mario = perso("SuperMarioWalk3.gif", mario.x, mario.y)
                mario.x += 5
                
    if jump == 1 and xaya<5 :
        if initjump == 0 :
            xaya = -5
            initjump = 1
        else :
            xaya += 1
        mario.y = round(-2/3*(xaya**2), 0)
    else :
        initjump = 0
        jump = 0

    fenetre.blit(fond, (0, 0))
    fenetre.blit(mario.image, (mario.x,mario.y))
    pygame.display.update()
    pygame.time.Clock().tick(60)