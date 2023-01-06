import pygame
from pygame.locals import *
from math import *
pygame.init()
sc = pygame.display.set_mode((600, 600))
red = (255, 0, 0)
blue = (100, 100, 255)
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (30, 60, 30)
sc.fill (black)
def draw_circle (c, x, y, r):
    pygame.draw.circle(sc, c, (int(300 + x), int(300 - y)), r)

def draw_line (c, x1, y1, x2, y2):
	pygame.draw.line(sc, c, (int(300 + x1), int(300 - y1) ),\
		(int(300 + x2), int(300 - y2) ), 4)
# -----------------
dt = 0.01
m = 1
x = 0
y = 200
vx = 10
vy = 0
G = 3e4
re = 5
draw_circle (blue, x, y, re)
draw_circle (yellow, 0, 0, 20)
pygame.display.update()
n = 100000
t = 0
cont = True
while cont:
	if t < n:
		t += 1
		r = hypot(x, y)
		f = -G / r**2
		ax = f * x / r
		ay = f * y / r
		vx += ax *dt
		vy += ay *dt
		x += vx *dt
		y += vy *dt
		draw_circle (blue, x, y, re)
		# ~ draw_circle (yellow, 0, 0, 20)
		pygame.display.update()
		# ~ sc.fill (black)

	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == pygame.K_ESCAPE or event.key == K_q:
					cont = False
		if event.type == QUIT:
			cont = False
pygame.image.save(sc,'Asteroid.jpeg')
pygame.quit()
