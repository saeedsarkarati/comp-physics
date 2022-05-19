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
    pygame.draw.circle(sc, c, (int(x), int(y)), r)
                          
# -----------------
xs = 300
ys = 300
rs = 40
res = 200
re = 10
rme = 40
rm = 3
t = 0
n = 10000
we = 2 * pi / n
wm = 13 * 2 * pi / n

xe = xs + res * cos (we * t)
ye = ys + res * sin (we * t)
xm = xe + rme * cos (wm * t)
ym = ye + rme * sin (wm * t)
draw_circle (yellow, xs, ys, rs)
draw_circle (white, xm, ym, rm)
draw_circle (blue, xe, ye, re)
# ---------------
pygame.display.update()

cont = True
while cont:
	if t < n:
		t += 1
		
	# ~ draw_circle (black, xe, ye, re)
	# ~ draw_circle (black, xm, ym, rm)
	xe = xs + res * cos (we * t)
	ye = ys + res * sin (we * t)
	xm = xe + rme * cos (wm * t)
	ym = ye + rme * sin (wm * t)
	draw_circle (white, xm, ym, rm)
	# ~ draw_circle (blue, xe, ye, re)
	pygame.display.update()

	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == pygame.K_ESCAPE or event.key == K_q:
					cont = False
		if event.type == QUIT:
			cont = False
pygame.image.save(sc,'moon_orbit.jpeg')
pygame.quit()
