class perso():
    def __init__(self, image, x=0, y=0, directionX=1, directionY=1):
        self.image = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y
        self.directionX = directionX
        self.directionY = directionY

    def vie(mavie, x=50, y=50):
      mavie = 5
     if perdu
        mavie = mavie-1
     print(mavie)



    def move(self):
        if self.x == 0:
            self.directionX = 1
        if self.x == screensize[0] - 60:
            self.directionX = -1
        if self.y == 0:
            self.directionY = 1
        if self.y == screensize[1] - 100:
            self.directionY = -1
        self.x += self.directionX
        self.y += self.directionY