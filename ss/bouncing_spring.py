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
    pygame.draw.circle(sc, c, (int(x), int(300 - y)), r)
                          
# -----------------
m = 0.1
k = 1
B = 0.03
v = 0
y = 200
n = 600
t = 0
r = 4
dt = 0.001
draw_circle (yellow, t, y, r)

pygame.display.update()
cont = True
while cont:
	# ~ draw_circle (black, t, y, r)
	if t < n:
		t += .1
		
		f = - k * y - B * v
		a = f / m
		v += a * dt
		y += v * dt
		draw_circle (yellow, t, y, r)
		pygame.display.update()

	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == pygame.K_ESCAPE or event.key == K_q:
					cont = False
		if event.type == QUIT:
			cont = False

pygame.image.save(sc,'bouncing_spring.jpeg')
pygame.quit()
