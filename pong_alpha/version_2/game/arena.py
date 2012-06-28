# ARENA.PY - controls orientation of game arena

import pyglet, resources

class Arena(pyglet.sprite.Sprite):
	def __init__(self, *args, **kwargs):
		super(Arena, self).__init__(img=resources.arena_image,*args,**kwargs)
		self.x
		
	def rotate(self, theta):
		self.rotation = theta