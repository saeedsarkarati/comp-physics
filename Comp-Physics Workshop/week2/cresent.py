import pygame
from pygame.locals import *
from math import *
pygame.init()
sc = pygame.display.set_mode((800,600))
co = (255, 255, 100)
l = (1, -1, -1)
ll = sqrt ( l[0] * l[0] + l[1] * l[1] + l[2] * l[2])
def sphere(x, y, r):
	for i in range(-r, r):
		for j in range(-r, r):
			if i * i + j * j < r * r :
				k = sqrt(r * r - i * i - j * j)
				c = l[0] * i + l[1] * j + l[2] * k
				if c > 0:
					d = c / (r * ll)
					dr = int (d * co[0])
					dg = int (d * co[1])
					db = int (d * co[2])
					cc = (dr, dg, db)
					sc.set_at((x + i,y + j), cc)
		
sphere(400, 300, 200)
pygame.display.update()
cont = True
while cont:
	for event in pygame.event.get():
		if event.type == QUIT:
			cont = False
