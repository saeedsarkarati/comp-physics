#~ PG001
import pygame
from pygame.locals import *
pygame.init()
sc = pygame.display.set_mode((800, 600))
#~ این چهار خط تقریبا همیشه در ابتدای برنامه‌های پایگیم می‌آیند.
#~ برنامه‌ٔ خود را زیر این چهار خط بنویسید.
#~ یعنی از اینجا....

sc.set_at((100, 100), (0, 255, 255))
pygame.display.update()

#~ ... تا اینجا
cont = True
while cont:
	for e in pygame.event.get():
		if e.type == QUIT:
			cont = False
pygame.quit()
