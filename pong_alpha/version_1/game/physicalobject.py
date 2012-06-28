# PHYSICALOBJECT.PY - defines behavior of objects

class PhysicalObject(pyglet.sprite.Sprite):
	def __init__(self, *args, **kwargs):
		super(PhysicalObject, self).__init__(*args, **kwargs)
		
		self.velocity_x, self.velocity_y = 0.0, 0.0
		
	def update(self, dt):
		self.x = self.velocity_x * dt
		self.y = self.velocity_y * dt
		self.check_bounds()
		
	def check_bounds(self):
		min_x = -self.image.width/2
		min_y = -self.image.height/2
		max_x = 800 + self.image.width/2
		max_y = 600 + self.image.height/2
		if self.x < min_x:
			self.velocity_x = -self.velocity_x
		elif self.x > max_x:
			self.velocity_x = -self.velocity_x
		if self.y < min_y:
			self.velocity_y = -self.velocity_y 
		elif self.y > max_y:
			self.velocity_y =-self.velocity_y
