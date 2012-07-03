# VISIBLEOBJECT.PY - defines behavior of visible clones

import pyglet, math, time
from pyglet.window import key

class VisibleObject(pyglet.sprite.Sprite):
	def __init(self, *args, **kwargs):
		super(VisibleObject, self).__init__(*args, **kwargs)
		self.record = []
		
	def update(self,twin,theta,game_window):
		theta_rad = math.radians(theta)
		tocenter_x = game_window.width/2
		tocenter_y = game_window.height/2

		dx = tocenter_x-(tocenter_x*math.cos(theta_rad) - tocenter_y*math.sin(theta_rad))
		dy = tocenter_y-(tocenter_x*math.sin(theta_rad) + tocenter_y*math.cos(theta_rad))

		self.x = (twin.x*math.cos(theta_rad) - twin.y*math.sin(theta_rad)) + dx
		self.y = (twin.x*math.sin(theta_rad) + twin.y*math.cos(theta_rad)) + dy

		self.make_record()

	def make_record(self):
		self.record.append(repr(self.x)+"\t"+repr(self.y)+"\t"+repr(time.time()))