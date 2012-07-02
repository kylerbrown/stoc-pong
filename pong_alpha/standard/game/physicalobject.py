# PHYSICALOBJECT.PY - defines behavior of objects

import pyglet
from pyglet.window import key

class PhysicalObject(pyglet.sprite.Sprite):	
	def __init__(self, *args, **kwargs):
		super(PhysicalObject, self).__init__(*args, **kwargs)
		self.velocity_x, self.velocity_y = 0.0, 0.0
		self.key_handler = key.KeyStateHandler()

	def check_bounds(self,dt,arena):
		arena_xl, arena_xr, arena_yl, arena_yr = arena.get_bounds()

		min_x = self.width/2 + (arena_xl + 7)
		min_y = self.height/2 + (arena_yl + 7)
		max_x = (arena_xr - 7) - self.width/2
		max_y = (arena_yr - 7) - self.height/2

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