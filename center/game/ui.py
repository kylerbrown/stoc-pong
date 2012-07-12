# UI.PY

from pyglet.window import key

class UI():
	def __init__(self,*args,**kwargs):
		self.gameState = "splash"
		self.key_handler = key.KeyStateHandler()
		
	def update(dt):
		if self.key_handler[key.UP]:
			self.gameState = "inPlay"
		if self.key_handler[key.SPACE]:
			self.gameState = "paused"
			if self.key_handler[key.ENTER]:
				self.gameState = "quit"
			if self.key_handler[key.SPACE]:
				self.gameState = "inPlay"
		