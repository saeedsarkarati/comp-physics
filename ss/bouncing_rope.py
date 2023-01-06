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
class Tmass:
	def __init__(self):
		self.mass = 1
		self.x = 0
		self.y = 0
		self.z = 0
		self.vx = 0
		self.vy = 0
		self.vz = 0
		self.fx = 0
		self.fy = 0
		self.fz = 0
	def eval (self):
		ax = self.fx / self.mass
		ay = self.fy / self.mass
		az = self.fz / self.mass
		self.vx += ax *dt
		self.vy += ay *dt
		self.vz += az *dt
		self.x += self.vx *dt
		self.y += self.vy *dt
		self.z += self.vz *dt
		


class Tspring:
	def __init__(self):
		self.m1 = None
		self.m2 = None
		self.k = 100
		self.ln = 1
	def len(self):
		l = sqrt ( (self.m1.x - self.m2.x) ** 2 +  \
		(self.m1.y - self.m2.y) ** 2 +  (self.m1.z - self.m2.z) ** 2  )
		return l
	def force(self):
		l = self.len() - self.ln
		f = - self.k * l
		self.m1.fx += f * (self.m1.x - self.m2.x) / self.len()
		self.m1.fy += f * (self.m1.y - self.m2.y) / self.len()
		self.m1.fz += f * (self.m1.z - self.m2.z) / self.len()
		self.m2.fx += f * (self.m2.x - self.m1.x) / self.len()
		self.m2.fy += f * (self.m2.y - self.m1.y) / self.len()
		self.m2.fz += f * (self.m2.z - self.m1.z) / self.len()
m=[]
nm = 6
nm1 = nm - 1
r = 100
h = 150
for i in range(nm):
	m.append(Tmass())
	if i < nm1:
		w = i * 2 * pi / nm1 
		m[i].x = r * cos(w)
		m[i].y = r * sin(w)
		m[i].z = h
		m[i].vx = r * cos(w + pi / 2)
		m[i].vy = r * sin(w + pi / 2)
		m[i].vz = 0
		
	else:
		m[i].x = 0
		m[i].y = 0
		m[i].z = -h
		m[i].vx = 0
		m[i].vy = 0
		m[i].vz = 0

# ~ mass[0].x = 10	
s =[]
ns = nm1*2
for i in range(ns):
	s.append(Tspring())
	if i < nm1:
		s[i].m1 = m[i]
		s[i].m2 = m[(i+1)%nm1]
	else:
		s[i].m1 = m[i - nm1]
		s[i].m2 = m[nm1]
	s[i].ln = s[i].len()

def draw():
	for i in range(nm):
		draw_circle (yellow, m[i].y, m[i].z, 5)
	for i in range(ns):
		draw_line( red, s[i].m1.y, s[i].m1.z, s[i].m2.y, s[i].m2.z) 
draw()

pygame.display.update()
n = 10000
t = 0
cont = True
while cont:
	if t < n:
		t += 1
		for i in range(nm):
			m[i].fx = 0
			m[i].fy = -0.1
			m[i].fz = 0
		for i in range(ns):
			s[i].force()
		for i in range(nm1):
			m[i].eval()
		sc.fill (black)
		draw()
		pygame.display.update()

	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == pygame.K_ESCAPE or event.key == K_q:
					cont = False
		if event.type == QUIT:
			cont = False
pygame.image.save(sc,'bouncing_rope.jpeg')
pygame.quit()
