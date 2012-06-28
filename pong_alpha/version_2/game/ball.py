# BALL.PY - controls the behavior of the ball

import pyglet, math, random, physicalobject
from pyglet.window import key
import resources
# import ui - will control user actions

class Ball(physicalobject.PhysicalObject):
	def __init__(self,*args,**kwargs):
		super(Ball,self).__init__(img=resources.ball_image,*args,**kwargs)
		self.scale = 0.5
		self.x = 300
		self.y = 300
		self.velocity_x = random.random() * 200 + 100
		self.velocity_y = random.random() * -200 - 100
		self.in_play = True

	def update(self,dt):
		if self.in_play == False:
			self.x += 0
			self.y += 0
		else:
			if self.check_bounds(dt) == "bound_xl" or self.check_bounds(dt) == "bound_xr":
				self.velocity_x = -self.velocity_x
				self.x += self.velocity_x * dt
			elif self.check_bounds(dt) == "bound_y":
				self.velocity_y = -self.velocity_y
				self.y += self.velocity_y * dt
			elif self.check_bounds(dt) == "drop":
				self.x = 300
				self.y = 500
				self.velocity_x = random.random() * 200 + 100
				self.velocity_y = random.random() * -200 - 100
			else:
				self.x += self.velocity_x * dt
				self.y += self.velocity_y * dt
		self.make_record(dt)

	def collides_with(self,paddle):
		min_y = self.scale * self.image.height/2 + paddle.y
		min_x = paddle.x - paddle.image.width/2
		max_x = paddle.x + paddle.image.width/2
		collision = self.y < min_y and (self.x > min_x and self.x < max_x)
		return(collision)

	def handle_collision(self, dt):
		self.velocity_y = - self.velocity_y
		self.y += self.velocity_y * dt