# GEOMETRY.PY - defines necessary geometric operations

import math, random

class Geometry():
	def __init__(self,constants,*args,**kwargs):
		# import game constants
		self.centerX = constants.centerX
		self.centerY = constants.centerY
	
	# returns the smallest representable number [UNUSED]
	'''
	def eps(self):
		x = 0.5
		while 0.0 + x != 0.0:
			epsilon = x
			x /= 2.0
		return epsilon
	'''

	def toPolar(self,xPos,yPos):
		xAdj = xPos - self.centerX
		yAdj = yPos - self.centerY
		radius = ( xAdj ** 2 + yAdj ** 2) ** .5
		theta = math.atan2( yAdj, xAdj )
		return radius, theta

	def fromPolar(self,radius,theta,):
		xAdj = radius * math.cos(theta)
		yAdj = radius * math.sin(theta)
		xPos = xAdj + self.centerX
		yPos = yAdj + self.centerY
		return xPos, yPos
	
	def movePaddle(self,xPos,yPos,speed,dt):
		radius, theta = self.toPolar(xPos,yPos)
		theta += speed * dt
		xPos, yPos = self.fromPolar(radius, theta)
		return xPos, yPos
	
	def orientPaddle(self,xPos,yPos):
		theta = math.atan2(yPos-self.centerY,xPos-self.centerX)
		return math.degrees(-theta)-90
		
	def randomAngle(self,speed):
		theta = random.random()*2*math.pi
		xVel = math.sin(theta) * speed
		yVel = math.cos(theta) * speed
		return xVel, yVel
	
	
