# PONG.PY - basic pong game

## LOAD MODULES
import pyglet, random, datetime, math
from pyglet.window import key
from game import resources, player, ball, arena, ui
from pyglet.gl import *

## INITIALIZE GAME ELEMENTS
# Initialize window
game_window = pyglet.window.Window(600, 600)
# Initialize batches
main_batch = pyglet.graphics.Batch()
alt_batch = pyglet.graphics.Batch()

# Initialize paddle and ball as sprites
arena = arena.Arena(batch=main_batch)
player_paddle = player.Player(x=300,y=50,batch=main_batch)
ball = ball.Ball(batch=main_batch)
game_flow = ui.UI(batch=main_batch)

# rotate paddle and ball 
#theta = 0
#ball.rotate_mov(theta,game_window)
#player_paddle.rotate_mov(theta,game_window)

# Initialize game objects to a list
game_objects = [player_paddle, ball, ui]

# Push key handler
game_window.push_handlers(player_paddle.key_handler)
game_window.push_handlers(ball.key_handler)
game_window.push_handlers(ui.key_handler)

## PAINT SCREEN
@game_window.event
def on_draw():
    # Clear screen
    game_window.clear()
    # draw game elements
    main_batch.draw()
    # alt_batch.draw()

def update(dt):
	for obj in game_objects:
		obj.update(dt)
	if ball.collides_with(player_paddle):
		ball.handle_collision(dt)
	ball.in_play = game_flow.in_play
	#if game_flow.quit_game:
	#	print_str="ball \t paddle \n"
	#	for i in range(len(ball.record)):
	#		print_str = print_str+repr(ball.record[i])+"\t"+repr(player_paddle.record[i])+"\n" 
	#	now = datetime.datetime.now()
	#	filename = now.strftime("%Y-%m-%d-%H-%M")
	#	print filename
	#	try:
	#		f = open("/Users/Alex/desktop/PONG!/data/"+filename+".txt", "w")
	#		try:
	#			f.write(print_str) 
	#		finally:
	#			f.close()
	#	except IOError:
	#		pass
	#	game_window.close()

# Tell pyglet to run the code
if __name__ == '__main__':
    # run update 120 time per second
    pyglet.clock.schedule_interval(update, 1/200.0)
    # run pyglet
    pyglet.app.run()
##