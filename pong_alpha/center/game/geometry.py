# GEOMETRY.PY

import math, random

def eps():
	x = 0.5
	while 0.0 + x != 0.0:
		epsilon = x
		x /= 2.0
	return epsilon

def toPolar(xPos,yPos,centerX,centerY):
	xAdj = xPos - centerX
	yAdj = yPos - centerY
	radius = ( xAdj ** 2 + yAdj ** 2) ** .5
	theta = math.atan2( yAdj, xAdj )
	return radius, theta

def fromPolar(radius,theta,centerX,centerY):
	xAdj = radius * math.cos(theta)
	yAdj = radius * math.sin(theta)
	xPos = xAdj + centerX
	yPos = yAdj + centerY
	return xPos, yPos
	
def movePaddle(xPos,yPos,speed,centerX,centerY,dt):
	radius, theta = toPolar(xPos,yPos,centerX,centerY)
	theta += speed * dt
	xPos, yPos = fromPolar(radius, theta,centerX,centerY)
	return xPos, yPos
	
def orientPaddle(xPos,yPos,centerX,centerY):
	theta = math.atan2(yPos-centerY,xPos-centerX)
	return math.degrees(-theta)-90
	
def randomAngle(speed):
	theta = random.random()*2*math.pi
	xVel = math.sin(theta) * speed
	yVel = math.cos(theta) * speed
	return xVel, yVel
	
	