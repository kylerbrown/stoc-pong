# CLONE.PY - controls behavior of the object clones

import resources, visibleobject

class Clone(visibleobject.VisibleObject):
	def __init__(self,*args,**kwargs):
		super(Clone,self).__init__(*args,**kwargs)
		self.record = []