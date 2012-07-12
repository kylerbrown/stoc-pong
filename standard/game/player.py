# PLAYER.PY - controls behavior of the paddle

import pyglet, math, physicalobject
from pyglet.window import key
import resources

class Player(physicalobject.PhysicalObject):
	def __init__(self,*args,**kwargs):
		super(Player,self).__init__(img=resources.player_image,*args,**kwargs)
		self.velocity_x = 500.0
		self.velocity_y = 0.0
		
	def update(self,dt,arena):
		arena_xl, arena_xr, arena_yl, arena_yr = arena.get_bounds()

		if self.key_handler[key.LEFT]:
			if self.check_bounds(dt,arena) == "bound_xl":
				self.x = self.x
				self.y = self.y
			else:
				self.x -= self.velocity_x * dt
				self.y -= self.velocity_y * dt
		
		if self.key_handler[key.RIGHT]:
			if self.check_bounds(dt,arena) == "bound_xr":
				self.x = self.x
				self.y = self.y
			else:
				self.x += self.velocity_x * dt
				self.y += self.velocity_y * dt