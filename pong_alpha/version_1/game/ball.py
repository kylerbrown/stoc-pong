# BALL.PY - controls the behavior of the ball

import pyglet, math, random
from pyglet.window import key
import resources
#import ui - will control user interactions

class Ball(pyglet.sprite.Sprite):
	def __init__(self,*args,**kwargs):
		super(Ball,self).__init__(img=resources.ball_image,*args,**kwargs)
		self.scale = 0.5
		self.x = 400
		self.y = 300
		self.velocity_x = random.random() * 200 + 100
		self.velocity_y = random.random() * -200 - 100
		self.in_play = False
		self.key_handler = key.KeyStateHandler()
		self.record = []
		self.quit_text = pyglet.text.Label(text="Quit Game? Y/N",x=400, y=300,anchor_x='center',*args,**kwargs)
		self.quit_text.color = (255,255,255,0)
		self.quit_option = False
		self.quit_game = False
		
	def update(self,dt):
		if self.key_handler[key.UP]:
			self.in_play = True
		if self.key_handler[key.SPACE]:
			self.in_play = False
			self.quit_text.color = (255,255,255,255)
			self.quit_option = True
		if self.quit_option:
			if self.key_handler[key.Y]:
				self.quit_game = True
			if self.key_handler[key.N]:
				self.in_play = True
		if self.in_play == False:
			self.x += 0
			self.y += 0
		else:
			self.x += self.velocity_x * dt
			self.y += self.velocity_y * dt
			self.check_bounds(dt)
			self.quit_text.color = (255,255,255,0)
		self.record.append([[self.x,self.y]])
		
	def check_bounds(self,dt):
		min_x = self.image.width/2
		min_y = self.image.height/2
		max_x = 800 - self.image.width/2
		max_y = 600 - self.image.height/2
		if self.x < min_x or self.x > max_x:
			self.velocity_x = -self.velocity_x
			self.x += self.velocity_x * dt
		if self.y > max_y:
			self.velocity_y = -self.velocity_y
			self.y += self.velocity_y * dt
		if self.y < min_y:
			self.x = 400
			self.y = 300
			self.velocity_x = random.random() * 200 + 100
			self.velocity_y = random.random() * -200 - 100

	def collides_with(self,paddle):
		min_y = self.scale * self.image.height/2 + paddle.y
		min_x = paddle.x - paddle.image.width/2
		max_x = paddle.x + paddle.image.width/2
		collision = self.y < min_y and (self.x > min_x and self.x < max_x)
		return(collision)
		
	def handle_collision(self, dt):
		self.velocity_y = - self.velocity_y
		self.y += self.velocity_y * dt