# PLAYER.PY - controls behavior of the paddle

import pyglet, math
from pyglet.window import key
import resources

class Player(pyglet.sprite.Sprite):
	def __init__(self,*args,**kwargs):
		super(Player,self).__init__(img=resources.player_image,*args,**kwargs)
		self.x = 400
		self.y = 50
		# Set movement speed
		self.velocity_x = 500.0
	    # Let pyglet handle keyboard events for us
		self.key_handler = key.KeyStateHandler()
		self.record = []
			
	def update(self,dt):
		min_x = self.image.width/2
		max_x = 800 - self.image.width/2
		if self.key_handler[key.LEFT]:
			if self.x < min_x:
				self.x = self.x
			else:
				self.x -= self.velocity_x * dt
		if self.key_handler[key.RIGHT]:
			if self.x > max_x:
				self.x = self.x
			else:
				self.x += self.velocity_x * dt
		self.record.append([[self.x, self.y]])