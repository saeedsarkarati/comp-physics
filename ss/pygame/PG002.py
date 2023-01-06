#~ PG002
import pygame
from pygame.locals import *
pygame.init()
sc = pygame.display.set_mode((800, 600))

def square (x , y, r):
	for i in range(-r, r):
		for j in range(-r, r):
			sc.set_at((x + i, y + j), (255, 255, 127))
	pygame.display.update()
def circle (x , y, r):
	for i in range(-r, r):
		for j in range(-r, r):
			if i * i + j *j <= r * r:
				sc.set_at((x + i, y + j), (0, 155, 255))
	pygame.display.update()
def ceresent (x , y, r):
	lx = 1
	ly = 0
	lz = -1
	for i in range(-r, r):
		for j in range(-r, r):
			if i * i + j *j < r * r:
				k = (r*r - i*i - j*j)**0.5
				c = i*lx + j*ly + k * lz
				if c > 0 :
					sc.set_at((x + i, y + j), (255, 255, 255))
	pygame.display.update()

def sphere (x , y, r):
	lx = 1
	ly = 1
	lz = 1
	l = (lx*lx + ly*ly + lz*lz)**0.5
	for i in range(-r, r):
		for j in range(-r, r):
			if i * i + j *j < r * r:
				k = (r*r - i*i - j*j)**0.5
				c = i*lx + j*ly + k * lz
				if c > 0 :
					cc = int (255 * c / (r * l) )
					sc.set_at((x + i, y + j), (cc, cc, cc))
	pygame.display.update()
square (50, 70, 40)
circle (70, 200, 60)
ceresent (700, 150, 70)
sphere (400, 300, 200)

cont = True
while cont:
	for e in pygame.event.get():
		if e.type == QUIT:
			cont = False
pygame.quit()
