# BALL.PY

import pyglet
from pyglet.window import key
import geometry, resources

class Ball(pyglet.sprite.Sprite):
	def __init__(self,*args,**kwargs):
		super(Ball,self).__init__(img=resources.ball_image,*args,**kwargs)
		self.speed = 100
		self.xVel, self.yVel = geometry.randomAngle(self.speed)
		
	def update(self,dt):
		self.x += self.xVel * dt
		self.y += self.yVel * dt