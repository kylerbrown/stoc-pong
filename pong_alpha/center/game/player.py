# PLAYER.PY

import pyglet, math
from pyglet.window import key
import geometry, resources

class Player(pyglet.sprite.Sprite):
	def __init__(self,constants,geometry,*args,**kwargs):
		super(Player,self).__init__(img=resources.player_image,*args,**kwargs)
		self.speed = 4
		self.key_handler = key.KeyStateHandler()
		# import geometric operations
		self.calc = geometry
		# set initial position from game constants
		self.x = constants.centerX
		yPos=constants.centerY-constants.gameRadius* \
			(1-(constants.pathWidth/constants.pathRadius)) 
		self.y = yPos

		
	def update(self,dt,constants):
		if self.key_handler[key.LEFT]:
			self.x, self.y = self.calc.movePaddle(self.x,self.y,-1*self.speed,
													dt)
		if self.key_handler[key.RIGHT]:
			self.x, self.y = self.calc.movePaddle(self.x,self.y,self.speed,
													dt)
		# keep paddle oriented correctly											 
		self.rotation = self.calc.orientPaddle(self.x,self.y)
		# find angular surface area of paddle
		self.subtend = math.atan2(self.width/2,constants.gameRadius)
		radius, self.theta = self.calc.toPolar(self.x,self.y)
		self.minTheta = self.theta - self.subtend
		self.maxTheta = self.theta + self.subtend
		
