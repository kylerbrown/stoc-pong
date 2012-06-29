# BALL_CLONE.PY - controls behavior of the ball clone

import resources, visibleobject

class BallClone(visibleobject.VisibleObject):
	def __init__(self,*args,**kwargs):
		super(BallClone,self).__init__(img=resources.ball_image,*args,**kwargs)
		self.scale = 0.5
		self.x = 300
		self.y = 300
		self.record = []