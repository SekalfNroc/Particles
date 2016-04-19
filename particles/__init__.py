class Object():
	instances = []

	def __init__(self, parts, opts={}):
		self.parts = parts
		self.opts = opts

		self.id = len(Object.instances)
		Object.instances.append(self)

	def __int__(self):
		return self.id

	def updateRecord(self):
		Object.instances[self.id] = self;

class Particle():
	instances = []

	def __init__(self, x, y):
		self.x = x
		self.y = y

		self.id = len(Particle.instances)
		Particle.instances.append(self)

	def __int__(self):
		return self.id

	def updateRecord(self):
		Particle.instances[self.id] = self;
		
class Bond():
	instances = []

	def __init__(self, A, B):
		self.A = A
		self.B = B

		self.id = len(Bond.instances)
		Bond.instances.append(self)

	def __int__(self):
		return self.id

	def updateRecord(self):
		Bond.instances[self.id] = self;
						
class Translation():
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Rotation():
	def __init__(self, x, y, angle):
		self.x = x
		self.y = y
		self.angle = angle
		
class PrimativeDrawer():
	def __init__(self):
		pass

	def rect(self, x, y, width, height, opts={}):
		parts = []
		bonds = []

		for i in range(x, x + width):
			for j in range(y, y + height):
				parts.append(int(Particle(i, j)))

		for p in parts:
			if not Particle.instances[p].x == x + width:
				bonds.append(int(Bond(p, p+1)))

			if not Particle.instances[p].y == y + height:
				bonds.append(int(Bond(p, p+width)))

		return Object(parts, opts)


