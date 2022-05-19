import pygame
from pygame.locals import *

radius=20

class tsquare:
    def __init__(self,x,y,r,red,green,blue):
        self.x=x
        self.y=y
        self.r=r
        self.red=red
        self.green=green
        self.blue=blue

class tspot(tsquare):
    def draw(self):
        for i in range(self.x-self.r, self.x+self.r):
            for j in range(self.y-self.r, self.y+self.r):
                rp, gp, bp, op=sc.get_at((i, j))
                rp = rp | self.red
                gp = gp | self.green
                bp = bp | self.blue
                sc.set_at((i, j),(rp, gp, bp))

class tfilter(tsquare):
    def draw(self):
        for i in range(self.x-self.r, self.x+self.r+1):
            for j in range(self.y-self.r, self.y+self.r+1):
                rp, gp, bp, op=sc.get_at((i, j))
                if(i==self.x-self.r or i==self.x+self.r or j==self.y-self.r or j==self.y+self.r):
                    rp,gp,bp = 255,255,255
                rp = rp & self.red
                gp = gp & self.green
                bp = bp & self.blue
                sc.set_at((i, j),(rp, gp, bp))

sq=[tspot(60,60, radius, 255, 0, 0),
      tspot(120,60, radius, 0, 255, 0),
      tspot(180,60, radius, 0, 0, 255),
      tfilter(240,60, radius, 255, 0, 0),
      tfilter(300,60, radius, 0, 255, 0),
      tfilter(360,60, radius, 0, 0, 255),
      tfilter(420,60, radius, 0, 255, 255),
      tfilter(480,60, radius, 255, 0, 255),
      tfilter(540,60, radius, 255, 255, 0)
      ]



pygame.init()
sc = pygame.display.set_mode((800, 600))

red = (255, 0, 0)
blue = (0, 0, 255)
def circle (c, p, r):
    pygame.draw.circle(sc, c, p, r)

# -----------------

for i in (sq):
    i.draw()

# ---------------
pygame.display.update()
index = 0
cont = True
dx, dy = 0, 0
while cont:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            for k in range(9):
                if int(event.key)-48 == k:
                    index = k
            if event.key == pygame.K_LEFT:
                dx = -1
            if event.key == pygame.K_RIGHT:
                dx = 1
            if event.key == pygame.K_UP:
                dy = -1
            if event.key == pygame.K_DOWN:
                dy = 1
        if event.type == KEYUP:
            if event.key == pygame.K_LEFT:
                dx = 0
            if event.key == pygame.K_RIGHT:
                dx = 0
            if event.key == pygame.K_UP:
                dy = 0
            if event.key == pygame.K_DOWN:
                dy = 0
            if event.key == pygame.K_ESCAPE or event.key == K_q:
                cont = False

        if event.type == QUIT:
            cont = False
            pygame.quit()

    sq[index].x+=dx
    sq[index].y+=dy
    sc.fill((0,0,0))
    for i in (sq):
        i.draw()
    pygame.display.update()
