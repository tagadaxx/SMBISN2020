import pygame
from Perso import perso
from pygame.locals import *

start = 0
xmomentum,ymomentum = 0,0
tempy= 0
points = 0
white = Color(255,255,255)
coordlist=[]
screensize = (897, 672)
pygame.init()
fenetre = pygame.display.set_mode(screensize, RESIZABLE)
continuer = True
RUN, PAUSE = 0, 1
etat = RUN
jump_sound = pygame.mixer.Sound("jump.wav")
jump = 0
walk = 0
initjump = 0
coins = 0
X=0
xaya=-10
MarioState = 0
walk = 0
orientation = "D"
liste1,liste2,liste3,liste4 = [],[],[],[]

fond = pygame.image.load("map.png").convert_alpha()
fond = pygame.transform.scale(fond, (10176, 672))
splash = pygame.image.load("Smb splash.png").convert_alpha()
splash = pygame.transform.scale(splash, (897,672))


pygame.key.set_repeat(1, 1)
mario = perso("MarioSmall.gif", 96, 528)


def resize(a,x,y):
    self =  pygame.transform.scale(a, (x,y))
    return self

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def message_display(text,a,b):
    largeText = pygame.font.Font('SuperMario256.ttf',25)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (a,b)
    fenetre.blit(TextSurf, TextRect)


""" 
with open("entities.txt", "r") as entities:
    for ligne in entities:
        liste= ligne[9:].split(";")
        liste.pop()
        for i in range(len(liste)):
            liste[i]=int(liste[i])
        print(ligne[0])
        if ligne[0] == "1" :
            ligne1 = len(liste)
        if ligne[0] == "2" :
            ligne2 = len(liste)
        if ligne[0] == "3" :
            ligne3 = len(liste)
        if ligne[0] == "4" :
            ligne4 = len(liste)
        coordlist += liste

print(liste1, liste2, liste3, liste4)
    print(coordlist)
    print(ligne1,ligne2,ligne3,ligne4)
for i in range (0,ligne1):
    liste1 += coordlist[i]
for i in range (ligne1 +1,ligne2):
    liste2 += coordlist[i]
for i in range (ligne2 +1,ligne3):
    liste3 += coordlist[i]
for i in range (ligne3 +1,ligne4):
    liste4 += coordlist[i]
"""
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
            quit()

        if event.type == KEYDOWN :
            if event.key == K_SPACE :
                start = 1
            if event.key == K_LEFT:
                orientation = "G"
                if walk < 1:
                    mario = perso("MarioSmallWalk1.gif", mario.x, mario.y)
                    mario.image = pygame.transform.flip(mario.image, True, False)
                    walk += 0.5
                elif 1 <= walk < 2:
                    mario = perso("MarioSmallWalk2.gif", mario.x, mario.y)
                    mario.image = pygame.transform.flip(mario.image, True, False)
                    walk += 0.5
                elif walk >= 2:
                    mario = perso("MarioSmallWalk3.gif", mario.x, mario.y)
                    mario.image = pygame.transform.flip(mario.image, True, False)
                    walk = 0
            if event.key == K_RIGHT:
                orientation = "D"
                if walk < 1:
                    mario = perso("MarioSmallWalk1.gif", mario.x, mario.y)
                    walk += 0.5
                elif 1 <= walk < 2:
                    mario = perso("MarioSmallWalk2.gif", mario.x, mario.y)
                    walk += 0.5
                elif walk >= 2:
                    mario = perso("MarioSmallWalk3.gif", mario.x, mario.y)
                    walk = 0
            if event.key == K_UP and jump == 0:
                jump = 1
                pygame.mixer.Sound.play(jump_sound)
                tempy = mario.y
                mario = perso("MarioJump.gif", mario.x, mario.y)
            if event.key == K_DOWN and MarioState == 1:
                mario = perso("mariocrouch.gif", mario.x, mario.y)

        if event.type == KEYUP :
            if event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT or event.key == KEYUP:
                mario = perso("MarioSmall.gif", mario.x, mario.y)

        if jump == 1 and xaya < 9:
            if initjump == 0:
                xaya = -10
                initjump = 1

    """    if jump == 1 and xaya < 9:
        if xaya > 0:
            xaya += 1
            mario.y -= round(-2 / 3 * (xaya ** 2), 0)
        else:
            xaya += 1
            mario.y += round(-2 / 3 * (xaya ** 2), 0)
        if xaya == 9:
            mario.y = tempy
            if MarioState == 0:
                mario = perso("MarioSmall.gif", mario.x, mario.y)
            if MarioState == 1:
                mario = perso("SuperMario.gif", mario.x, mario.y)

    else:
        jump = 0
        xaya = -10"""
    if event.type == KEYDOWN :
        if event.key == K_RIGHT and xmomentum<40:
            xmomentum += 1
        if event.key == K_LEFT and xmomentum>-40 :
            xmomentum += -1
        if event.key == K_UP and jump == 0 :
            ymomentum -= 20
            jump = 1
    else :
        xmomentum = xmomentum/2
        if mario.y+48 > 576 :
            ymomentum = ymomentum+5
        jump = 0
    mario.x += xmomentum
    mario.y+= ymomentum


    if mario.x >= 448 :
        X -= 4
        mario.x -= 4


    if MarioState == 0:
        mario.image = resize(mario.image, 42, 48)
    elif MarioState == 1 or MarioState == 2:
        mario.image = resize(mario.image, 48, 80)

    if start == 0 :
        fenetre.blit(splash,(0,0))
    if start == 1 :
        fenetre.blit(fond, (X, 0))
        fenetre.blit(mario.image, (round(mario.x,0),round(mario.y,0)))
    message_display("score : "+str(points), 70, 30)
    message_display('coins : '+str(coins), 70, 60)


    pygame.display.update()
    pygame.time.Clock().tick(60)
