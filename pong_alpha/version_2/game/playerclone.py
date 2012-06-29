# PLAYERCLONE.PY - controls behavior of the paddle clone

import resources, visibleobject

class PlayerClone(visibleobject.VisibleObject):
	def __init__(self,*args,**kwargs):
		super(PlayerClone,self).__init__(img=resources.player_image,*args,**kwargs)
		self.record = []
