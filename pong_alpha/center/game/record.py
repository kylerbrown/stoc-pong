# RECORD.PY

import time

class Record():
	def __init__(self,gameObject,*args,**kwargs):
		self.x = gameObject.x
		self.y = gameObject.y
		self.data = []
		self.time = time.time
		
	def update(self, dt):
		now = self.time()
		self.data.append(repr(self.x)+"\t"+repr(self.y)+"\t"+repr(now)+"\n")