import pygame

########## intialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('background.jpg').convert()

############ Player
playerimg = pygame.image.load('player.png')
playerX = 400
playerY = 530
playerSpeed = 1
def player():
    global playerX
    global playerY
    if playerX == 800:
        playerX= 2
    if playerX == 1:
        playerX = 799
    screen.blit(playerimg, (playerX, playerY))

############# Alien
alienimg = pygame.image.load('alien.png')
class alien:
    def __init__(self,x,y):
        self.X = x
        self.Y = y
        self.speed = 1
        self.dir = 1                      #### used to pecify the direction of motion of alien
    def print(self):
        if self.X == 736:
            self.X = 735
            self.Y += 60
            self.dir += 1
        if self.X == 1:
            self.X = 2
            self.Y += 60
            self.dir += 1
        screen.blit(alienimg, (self.X, self.Y))

aliens=[]
a1=alien(1,1)
aliens.append(a1)
a2=alien(700,61)
aliens.append(a2)
a3=alien(400,1)
aliens.append(a3)

############ Bullet
bulletimg = pygame.image.load('bullet.png')
class bullet:
    def __init__(self,x):
        self.X = x+16
        self.Y = 510
        self.speed = 5

    def print(self):
        screen.blit(bulletimg, (self.X, self.Y))

############ Collision
def distance(x1,y1,x2,y2):
    return pow(pow(x2-x1,2)+pow(y2-y1,2),0.5)

########### Main game loop
running = True
bflag = 0
while running:

    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:                   ######## help quit the game
            running = False

    for a in aliens:
        if (a.dir % 2 != 0):
            if (a.Y > 490):
                running = False
            else:
                a.X += a.speed
                a.print()  ######## alien movement
        else:
            if (a.Y > 490):
                running = False
            else:
                a.X -= a.speed
                a.print()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX-=playerSpeed                        ######### player movement
        if event.key == pygame.K_RIGHT:
            playerX+=playerSpeed

    if bflag == 0:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                b1 = bullet(playerX)
                bflag = 1                              ########## Bullet
    if bflag == 1:
        if b1.Y < 5:
            bflag = 0
        else:
            for a in aliens:
                if distance(a.X+32,a.Y+2,b1.X+16,b1.Y) < 32:
                    bflag=0
                    a.X = 1
                    a.Y = 1
                    a.dir = 1
            b1.Y -= b1.speed
            b1.print()

    player()
    pygame.display.update()

