# UI.PY - control user interaction with the game window

import pyglet
from pyglet.window import key

class UI():
	def __init__(self,game_window,*args,**kwargs):
		self.key_handler = key.KeyStateHandler()
		center_x = game_window.width/2
		center_y = game_window.height/2
		self.quit_text = pyglet.text.Label(text="Quit Game? Y/N",x=center_x, y=center_y,anchor_x='center',*args,**kwargs)
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