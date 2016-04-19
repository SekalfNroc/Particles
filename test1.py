from particles import *

drawer = PrimativeDrawer()
obj = drawer.rect(10, 10, 100, 100)

for p in obj.parts:
	part = Particle.instances[p]
	pos = (part.x, part.y)
	print(pos)