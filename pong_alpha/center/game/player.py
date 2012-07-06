# PLAYER.PY

import pyglet
from pyglet.window import key
import geometry, resources

class Player(pyglet.sprite.Sprite):
	def __init__(self,originX,originY,*args,**kwargs):
		super(Player,self).__init__(img=resources.player_image,*args,**kwargs)
		self.speed = 4
		self.key_handler = key.KeyStateHandler()
		self.originX = originX
		self.originY = originY
		
	def update(self,dt):
		if self.key_handler[key.LEFT]:
			self.x, self.y = geometry.movePaddle(self.x,self.y,-1*self.speed,self.originX,self.originY,dt)
		if self.key_handler[key.RIGHT]:
			self.x, self.y = geometry.movePaddle(self.x,self.y,self.speed,self.originX,self.originY,dt) 
		self.rotation = geometry.orientPaddle(self.x,self.y,self.originX,self.originY)