# UI.PY - controls user interface

import pyglet

def game_paused(batch):
	level_label = pyglet.text.Label(text="Pong!", 
                                x=400, y=575,anchor_x='center',batch=alt_batch)