# ARENACLONE.PY - controls orientation of arena clone

import resources, visibleobject

class ArenaClone(visibleobject.VisibleObject):
	def __init__(self, *args, **kwargs):
		super(ArenaClone, self).__init__(img=resources.arena_image,*args,**kwargs)
		self.x = 300
		self.y = 300
		