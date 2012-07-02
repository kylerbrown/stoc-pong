# BALL.PY - controls the behavior of the ball

import pyglet, math, random, physicalobject
from pyglet.window import key
import resources
# import ui - will control user actions

class Ball(physicalobject.PhysicalObject):
	def __init__(self,*args,**kwargs):
		super(Ball,self).__init__(img=resources.ball_image,*args,**kwargs)
		self.vel = 220
		self.gen_rand_angle(self.vel)
		self.in_play = True

	def update(self,dt,arena,game_window):
		rand_x = 0
		rand_y = 0

		if self.in_play == False:
			self.x += 0
			self.y += 0
		else:
			if self.check_bounds(dt,arena) == "bound_xl":
				self.velocity_x = -self.velocity_x
				self.x += 2*(self.velocity_x * dt)
			elif self.check_bounds(dt,arena) == "bound_xr":
				self.velocity_x = -self.velocity_x
				self.x += 2*(self.velocity_x * dt)
			elif self.check_bounds(dt,arena) == "bound_y":
				self.velocity_x = self.velocity_x
				self.velocity_y = -self.velocity_y
				self.y += 2*(self.velocity_y * dt)
			elif self.check_bounds(dt,arena) == "drop":
				self.x = game_window.width/2
				self.y = game_window.height/2
				self.gen_rand_angle(self.vel)
			else:
				if random.random() < 0.0:
					rand_x = random.random() * 10
					rand_y = random.random() * 10
				self.x += self.velocity_x * dt + rand_x
				self.y += self.velocity_y * dt + rand_y

	def gen_rand_angle(self, vel):
		angle = math.radians((random.random() * 50) - 25)
		self.velocity_x = math.sin(angle) * vel
		self.velocity_y = math.cos(angle) * -vel

	def collides_with(self,paddle):
		min_y = self.height/2 + paddle.y + paddle.height/2
		min_x = paddle.x - paddle.width/2
		max_x = paddle.x + paddle.width/2
		collision = (self.y < min_y) and (self.y > min_y - 5) and (self.x > min_x and self.x < max_x)
		return(collision)

	def handle_collision(self, dt):
		self.velocity_y = - self.velocity_y
		self.velocity_x = self.velocity_x
		self.y += self.velocity_y * dt
		self.x += self.velocity_x * dt