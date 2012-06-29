# ARENA.PY - controls orientation of game arena

import pyglet, resources

class Arena(pyglet.sprite.Sprite):
	def __init__(self, *args, **kwargs):
		super(Arena, self).__init__(img=resources.arena_image,*args,**kwargs)
		self.x = 300
		self.y = 300
		
	def rotate(self, theta):
		self.rotation = theta

	def get_bounds(self):
		arena_xl = self.x - self.width/2
		arena_xr = self.x + self.width/2
		arena_yl = self.y - self.height/2
		arena_yr = self.y + self.height/2
		
		return arena_xl, arena_xr, arena_yl, arena_yr