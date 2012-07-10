# BALL.PY

import pyglet, math
from pyglet.window import key
import geometry, resources, record

class Ball(pyglet.sprite.Sprite):
	def __init__(self,constants,geometry,*args,**kwargs):
		super(Ball,self).__init__(img=resources.ball_image,*args,**kwargs)
		self.speed = 100
		# import geometric operations
		self.calc = geometry
		self.xVel, self.yVel = self.calc.randomAngle(self.speed)
		# import constants
		self.x = constants.centerX
		self.y = constants.centerY
		self.maxRadius = constants.gameRadius
	
	def checkBounds(self,paddle):
		radiusBall, thetaBall = self.calc.toPolar(self.x,self.y)
		if radiusBall > (self.maxRadius - 5):
			return "drop"
		elif radiusBall > (self.maxRadius - 10) and \
			(thetaBall > paddle.minTheta and thetaBall < paddle.maxTheta):
			return "collision"
		elif radiusBall < 1 and radiusBall > -1:
			return "center"
		else:
			return "in bounds"
			
	def update(self,dt,paddle,constants):
		status = self.checkBounds(paddle)
		if status == "in bounds":
			self.x += self.xVel * dt
			self.y += self.yVel * dt
		elif status == "collision":
			boost = .1
			self.xVel = -self.xVel
			self.yVel = -self.yVel
			self.x += boost*(self.xVel )
			self.y += boost*(self.yVel )
		elif status == "drop":
			self.x = constants.centerX
			self.y = constants.centerY
		elif status == "center":
			self.xVel, self.yVel = self.calc.randomAngle(self.speed)
			self.x += self.xVel * dt
			self.y += self.yVel * dt
		
		
