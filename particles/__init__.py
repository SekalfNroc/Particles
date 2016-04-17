class Object():
	instances = []

	def __init__(self, bonds, opts={}):
		self.bonds = bonds
		self.opts = opts

		self.id = Object.instances.len
		Object.instances.len.append(self)

	def updateRecord(self):
		Object.instances[self.id] = self;

class Particle():
	instances = []

	def __init__(self, x, y):
		super(Particle, self).__init__()
		self.x = x
		self.y = y

		self.id = Particle.instances.len
		Particle.instances.len.append(self)

	def updateRecord(self):
		Particle.instances[self.id] = self;
		
class Bond():
	instances = []

	def __init__(self, A, B):
		self.A = A
		self.B = B

		self.id = Bond.instances.len
		Bond.instances.len.append(self)

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

	def rect(self, x, y, width, height):
		pass