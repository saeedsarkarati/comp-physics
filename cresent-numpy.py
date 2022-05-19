import pygame
from pygame.locals import *
import numpy as np
pygame.init()
sc = pygame.display.set_mode((800,800))
fpsClock = pygame.time.Clock()
r = 300
d = r * 2 + 1
nd = d * d
pix = np.zeros(nd)
pic = pix.reshape(d, d)
co = (255, 255, 100)
lx , ly, lz = (1, -1, 0.5)
x0, y0, = 400, 400
i = np.zeros(nd, dtype = np.int)
ixy = i.reshape(d, d)

j = np.zeros(nd, dtype = np.int)
jxy = j.reshape(d, d)

ii = np.arange(-r,1)
jj = ii[:,np.newaxis]
ixy[:r+1, :] = jj[:]

ii = np.arange(1, r+1)
jj = ii[:,np.newaxis]
ixy[r+1:, :] = jj[:]

ii = np.arange(-r,1)
jj = ii[np.newaxis,:]
jxy[:, :r+1] = jj[:]

ii = np.arange(1, r+1)
jj = ii[np.newaxis,:]
jxy[:, r+1:] = jj[:]

kxy = (np.ones(nd).reshape(d,d) * r*r- ixy * ixy - jxy * jxy)
ixy[kxy<=0] = 0
jxy[kxy<=0] = 0
kxy[kxy<=0] = 0
kxy = np.sqrt(kxy) 
# ~ print (ixy)
# ~ print (jxy)
# ~ print (kxy)
rr1= np.zeros_like(kxy)
rr1[:] = np.random.randint(100)
rr2= np.zeros_like(kxy)
rr2[:] = np.random.randint(100)

def sphere():
	
	lz = np.cos(theta)
	ls = np.sin(theta)
	lx = ls * np.cos(phi)
	ly = ls * np.sin(phi)

	
	ccxy = (255 * (kxy * lz + ixy * lx + jxy * ly ) / (r)).astype(int)
	ccxy[ccxy<0] = 0
	ccxy[ccxy>255] = 255
	# ~ print (rr)
	# ~ ccxy[rr1<50]//=2
	ccxy[rr2<20]//=4
	# ~ print (ccxy)
	st = np.zeros((d, d, 3), dtype = np.int32)
	st[:,:,0] = ccxy[:,:]
	# ~ st[:,:,0][st[:,:,0] < 10] = 20
	st[:,:,1] = ccxy[:,:]
	st[:,:,2] = ccxy[:,:]
	su = pygame.surface.Surface((d,d))
	pygame.surfarray.blit_array(su, st)
	sc.blit(su, (x0 - r,y0 - r))

theta, phi = (0, 0)
vtheta = 0
vphi = 0

sphere()
cont = True
fpsClock.tick(30)

while cont:
	for event in pygame.event.get():
		if event.type == QUIT:
			cont = False
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				vphi = np.pi/100
			if event.key == K_RIGHT:
				vphi = -np.pi/100
			if event.key == K_UP:
				vtheta = np.pi/100
			if event.key == K_DOWN:
				vtheta = -np.pi/100
		if event.type == KEYUP:
			if event.key == K_LEFT:
				vphi = 0
			if event.key == K_RIGHT:
				vphi = 0
			if event.key == K_UP:
				vtheta = 0
			if event.key == K_DOWN:
				vtheta = 0
			if event.key == K_s:
				
				pygame.image.save(sc, 'moon.png')

	theta += vtheta
	phi += vphi
	sc.fill((0,0,0))
	sphere()
	pygame.display.update()















