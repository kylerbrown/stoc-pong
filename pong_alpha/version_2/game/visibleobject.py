# VISIBLEOBJECT.PY - defines behavior of visible clones

import pyglet, math, time
from pyglet.window import key

class VisibleObject(pyglet.sprite.Sprite):
	def __init(self, *args, **kwargs):
		super(VisibleObject, self).__init__(*args, **kwargs)
		self.record = []
		
	def update(self,twin,theta,game_window):
		theta_rad = math.radians(theta)
		d = game_window.width/2

		dx = 300-(300*(math.cos(theta_rad) - math.sin(theta_rad)))
		dy = 300-(300*(math.sin(theta_rad) + math.cos(theta_rad)))

		self.x = (twin.x*math.cos(theta_rad) - twin.y*math.sin(theta_rad)) + dx
		self.y = (twin.x*math.sin(theta_rad) + twin.y*math.cos(theta_rad)) + dy

		self.make_record()

	def make_record(self):
		self.record.append([self.x,self.y,time.time()])