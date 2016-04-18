from particles import *

drawer = PrimativeDrawer()
drawer.rect(10, 10, 100, 100)

for p in Particle.instances:
	print('(%d, %d)' % (p.x, p.y))