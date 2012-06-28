# UI.PY - control user interaction with the game window

import pyglet

class UI(pyglet.sprite.Sprite):
	def __init__(self,*args,**kwargs):
		super(Ball,self).__init__(*args,**kwargs)
		self.key_handler = key.KeyStateHandler()
		self.quit_text = pyglet.text.Label(text="Quit Game? Y/N",x=300, y=300,anchor_x='center',*args,**kwargs)
		self.quit_text.color = (255,255,255,0)
		self.quit_game = False
		self.in_play = False
		
	def update(self,dt):
		if self.in_play:
			self.quit_text.color = (255,255,255,0)
		if self.key_handler[key.UP]:
			self.in_play = True
		if self.key_handler[key.SPACE]:
			self.in_play = False
			self.quit_text.color = (255,255,255,255)
		if not self.in_play:
			if self.key_handler[key.Y]:
				self.quit_game = True
			if self.key_handler[key.N]:
				self.quit_game = False
		