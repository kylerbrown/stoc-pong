# PHYSICALOBJECT.PY - defines behavior of objects

import pyglet, math
from pyglet.window import key

class PhysicalObject(pyglet.sprite.Sprite):	
	def __init__(self, *args, **kwargs):
		super(PhysicalObject, self).__init__(*args, **kwargs)
		self.velocity_x, self.velocity_y = 0.0, 0.0
		self.record = []
		self.key_handler = key.KeyStateHandler()
		
	def rotate_mov(self,theta,game_window):
		self.rotation = -theta
		theta_rad = math.radians(theta)
		d = game_window.width/2 

		# Calculate new position
		self.x = self.x - (d * (math.cos(theta_rad) - math.sin(theta_rad)))
		self.y = self.y + (d * (math.cos(theta_rad) + math.sin(theta_rad)))

		# Calculate new velocity
		theta_o = math.atan(self.velocity_y/self.velocity_x)
		velocity = math.sqrt((self.velocity_y)**2 + (self.velocity_x)**2)
		theta_total = theta_rad + theta_o
		self.velocity_x = math.cos(theta_total) * velocity
		self.velocity_y = math.sin(theta_total) * velocity
		

	def check_bounds(self,dt):
		min_x = self.image.width/2
		min_y = self.image.height/2
		max_x = 600 - self.image.width/2
		max_y = 600 - self.image.height/2

		if self.x < min_x:
			return "bound_xl"
		elif self.x > max_x:
			return "bound_xr"
		elif self.y > max_y:
			return "bound_y"
		elif self.y < min_y:
			return "drop"
		else:
			return "okay"
			
	def make_record(self, dt):
		self.record.append([self.x,self.y])

