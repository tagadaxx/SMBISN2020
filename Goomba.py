import pygame
class Goomba(pygame.sprite.Sprite):
    def __init__(self,image,x,y,):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("goomba.gif").convert_alpha()
        def_init__(self,image,x,y,center)
        self.rect = self.image.get_rect
        self.x = x
        self.y = y
        self.rect.center = center

    def mouvement(self,a):
        if a == 0 :



"""enemy_group1 = pg.sprite.Group(goomba0)
        enemy_group2 = pg.sprite.Group(goomba1)
        enemy_group3 = pg.sprite.Group(goomba2, goomba3)
        enemy_group4 = pg.sprite.Group(goomba4, goomba5)
        enemy_group5 = pg.sprite.Group(goomba6, goomba7,goomba8)
        enemy_group7 = pg.sprite.Group(goomba9)
        enemy_group8 = pg.sprite.Group(goomba10, goomba11)
        enemy_group9 = pg.sprite.Group(goomba12, goomba13,goomba14)
        enemy_group10 = pg.sprite.Group(goomba15)

 self.enemy_group_list = [enemy_group1,
                                 enemy_group2,
                                 enemy_group3,
                                 enemy_group4,
                                 enemy_group5,
                                 enemy_group7,
                                 enemy_group8,
                                 enemy_group9,
                                 enemy_group10]
"""