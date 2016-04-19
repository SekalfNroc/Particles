import pygame, time
from particles import *

pygame.init()

disp = pygame.display.set_mode((1770, 980), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)
disp.fill((255, 255, 0))

drawer = PrimativeDrawer()
rectA = drawer.rect(200,  50, 100, 300, {'col': (255, 0, 0)})
rectB = drawer.rect(500, 200, 300, 100, {'col': (0, 0, 255)})

def drawRect(rect):
	for p in rect.parts:
		part = Particle.instances[p]
		pos = (part.x, part.y)
		pygame.draw.line(disp, rect.opts['col'], pos, pos)

drawRect(rectA)
drawRect(rectB)

pygame.display.update()

time.sleep(5)