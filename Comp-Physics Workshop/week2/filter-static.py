
import pygame
from pygame.locals import *

radius=80
d = 180

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

sq=[tspot(d,260, radius, 255, 0, 0),
      tspot(2*d,260, radius, 0, 255, 0),
      tspot(3*d,260, radius, 0, 0, 255),
      tfilter(4*d,260, radius, 255, 0, 0),
      ]



pygame.init()
sc = pygame.display.set_mode((1000, 1000))

# -----------------
'''
sq[2].x=120
sq[2].y=80
sq[0].red=255
sq[0].green=128
sq[0].blue=0
'''
sq[1].x = 260
sq[2].y = 350
sq[2].x = 210
sq[3].x = 290
sq[3].y = 320
sq[3].green = 255
for i in (sq):
    i.draw()

# ---------------
pygame.display.update()
cont = True

while cont:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == K_q:
                cont = False

        if event.type == QUIT:
            cont = False
            pygame.quit()
