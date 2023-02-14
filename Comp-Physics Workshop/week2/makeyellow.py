
import pygame
from pygame.locals import *
sc = pygame.display.set_mode((800,600))
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
pink = (255, 127, 127)
blue = (0, 0, 255)


# ---------
def square (x, y, r, red, green, blue):
	for i in range (-r, r):
		for j in range (-r, r):
			sc.set_at((x + i, y + j), (red, green, blue))
def circle (x, y, r, red, green, blue):
	for i in range (-r, r):
		for j in range (-r, r):
			if i * i + j * j <= r * r:
				sc.set_at((x + i, y + j), (red, green, blue))
def cresent (x, y, r, red, green, blue):
	lx = 1; ly = 1; lz = 2
	l = (lx * lx + ly * ly + lz * lz)**0.5
	lx = lx / l; ly = ly / l; lz = lz / l; 
	for i in range (-r, r):
		for j in range (-r, r):
			if i * i + j * j <= r * r:
				k = (r*r - i*i - j*j)**0.5
				ii = i / r; jj = j / r; kk = k / r
				dp = lx * ii + ly * jj + lz * kk
				if dp < 0:
					sc.set_at((x + i, y + j), (red, green, blue))
def sphere (x, y, r, red, green, blue):
	lx = 1; ly = 1; lz = -2
	l = (lx * lx + ly * ly + lz * lz)**0.5
	lx = lx / l; ly = ly / l; lz = lz / l; 
	for i in range (-r, r):
		for j in range (-r, r):
			if i * i + j * j <= r * r:
				k = (r*r - i*i - j*j)**0.5
				ii = i / r; jj = j / r; kk = k / r
				dp = lx * ii + ly * jj + lz * kk
				if dp < 0:
					c = -dp
					sc.set_at((x + i, y + j), (c*red, c*green, c*blue))
# ~ square ( 300, 300, 200, 0, 55, 0)
# ~ cresent ( 300, 300, 200, 255, 255, 160)
sphere ( 300, 300, 200, 255, 255, 160)

# ---------------
pygame.display.update()
cont = True

while cont:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE or event.key == K_q:
                cont = False

        if event.type == QUIT:
            cont = False
            pygame.quit()
