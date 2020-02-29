import pygame
from Perso import perso
from platforms import Platform
from pygame.locals import *

blocks = [(20,8),(22,8),(24,8),(78,8),(80,8),(81,4),(82,4),(83,4),(85,4),(86,4),(87,4),(88,4),(91,4),(92,4),(93,4),(94,8),(100,8),(101,8),(117,8),(120,4),(121,4),(122,4),(127,4),(128,8),(129,8),(130,4),(168,8),(169,8),(171,8),(198,11)]
luckbl = [(16,8,10),(22,4,10),(21,8,11),(23,8,10),(79,8,11),(94,4,10),(107,8,10),(109,8,10),(109,4,12),(111,8,10),(129,4,10),(130,4,10),(170,4,10)]
hardbl = [(134,11),(135,10),(136,9),(137,8),(140,8),(141,9),(142,10),(143,11),(148,11),(149,10),(150,9),(151,8),(152,8),(155,8),(156,9),(157,10),(158,11),(181,11),(182,10),(183,9),(184,8),(185,7),(186,6),(187,5),(188,4),(189,4)]
pipOr = [(29,10,2),(39,9,3),(47,8,4),(58,8,4),(163,10,2),(179,10,2)]

pygame.init()
start = 0
xmomentum,ymomentum = 0,0
points = 0
white = Color(255,255,255)
coordlist=[]
screensize = (897, 672)
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
MarioState = 0
walk = 0
orientation = "D"
liste1,liste2,liste3,liste4 = [],[],[],[]

fond = pygame.image.load("map.png").convert_alpha()
fond = pygame.transform.scale(fond, (10176, 672))
splash = pygame.image.load("Smb splash.png").convert_alpha()
splash = pygame.transform.scale(splash, (897,672))
blocplein = Platform(960, 384, 48, 48, "BlocPlein.gif")
brique = Platform(960, 384, 48, 48, "brique.gif")


pygame.key.set_repeat(100, 25)
mario = perso("MarioSmall.gif", 96, 528)


def resize(a,x,y):
    self = pygame.transform.scale(a, (x,y))
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
                pygame.mixer.Sound.play(jump_sound)
                mario = perso("MarioJump.gif", mario.x, mario.y)
            if event.key == K_DOWN and MarioState == 1:
                mario = perso("mariocrouch.gif", mario.x, mario.y)

        if event.type == KEYUP :
            if event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT or event.key == K_UP:
                mario = perso("MarioSmall.gif", mario.x, mario.y)


        if event.type == KEYDOWN :
            if event.key == K_RIGHT and xmomentum<7:
                xmomentum += 0.6
            if event.key == K_LEFT and xmomentum>-7 :
                xmomentum -= 0.6
            if event.key == K_UP and jump == 0 :
                ymomentum = -10

    '''if mario.y < 526:
        pass
    else :
        pass'''
    mario.x += xmomentum
    if ymomentum!=0 and 0<=jump<=200:
        mario.y += ymomentum
        jump-=ymomentum
    elif jump>=200:
        jump=200
        ymomentum=-ymomentum
    elif jump<0:
        jump=0
        ymomentum=0


    if mario.x >= 448 :
        X -= xmomentum
        mario.x -= xmomentum
    xmomentum=xmomentum-.15 if xmomentum>0 else xmomentum+.15


    if MarioState == 0:
        mario.image = resize(mario.image, 42, 48)
    elif MarioState == 1 or MarioState == 2:
        mario.image = resize(mario.image, 48, 80)

    if start == 0 :
        fenetre.blit(splash,(0,0))
    if start == 1 :
        fenetre.blit(fond, (X, 0))
        message_display("score : " + str(points), 70, 30)
        message_display('coins : ' + str(coins), 70, 60)
        #pygame.draw.rect(fenetre, white, pygame.Rect(0, 0, 10176, 672))
        for i in range(0, len(blocks)-1):
            fenetre.blit(brique.image, (blocks[i][0]*48 + X, blocks[i][1]*48))
        for i in range(0, len(hardbl) - 1):
            fenetre.blit(blocplein.image, (hardbl[i][0] * 48 + X, hardbl[i][1] * 48))
        fenetre.blit(mario.image, (round(mario.x,0),round(mario.y,0)))


    pygame.display.update()
    pygame.time.Clock().tick(80)