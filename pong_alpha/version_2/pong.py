# PONG.PY - basic pong game

import pyglet, random, datetime, math, time
from pyglet.window import key
from game import resources, player, ball, arena, ui
from game import clone
from pyglet.gl import *

# Initialize window
game_window = pyglet.window.Window(600, 600)

# Initialize batches
main_batch = pyglet.graphics.Batch()

# Set theta
theta = 45

## Initialize paddle, ball, and clones as sprites
# Arena
arena = arena.Arena(batch=main_batch)
arena.visible = False
arena_clone = clone.Clone(img=resources.arena_image,x=300,y=300,batch=main_batch)
arena_clone.rotation = -theta

# Paddle
paddle_scale = 0.5
player_paddle = player.Player(x=300,y=175,batch=main_batch)
player_paddle.visible = False
player_paddle.scale = paddle_scale
player_clone = clone.Clone(img=resources.player_image,batch=main_batch)
player_clone.rotation = -theta
player_clone.scale = paddle_scale

# Synchronization pixel
sync_pixel = ball.Ball(batch=main_batch)
sync_pixel.visible = False
sync_pixel.scale = 0.1
sync_pixel.x = 5
sync_pixel.y = 5
global pix_record
pix_record = []

# Ball
ball_scale = 0.3
ball = ball.Ball(batch=main_batch)
ball.visible = False
ball.scale = ball_scale
ball_clone = clone.Clone(img=resources.ball_image,batch=main_batch)
ball_clone.scale = ball_scale

# Game Flow
game_flow = ui.UI(batch=main_batch)

# Push key handlers
game_window.push_handlers(player_paddle.key_handler)
game_window.push_handlers(ball.key_handler)
game_window.push_handlers(game_flow.key_handler)

# Paint screen
@game_window.event
def on_draw():
    # Clear screen
    game_window.clear()
    # draw game elements
    main_batch.draw()

def update(dt,theta,arena,pix_record):
	ball.update(dt,arena)
	ball_clone.update(ball,theta,game_window)

	player_paddle.update(dt,arena)
	player_clone.update(player_paddle,theta,game_window)
	
	game_flow.update(dt)

	if ball.collides_with(player_paddle):
		ball.handle_collision(dt)

	ball.in_play = game_flow.in_play

	if game_flow.quit_game:
		print_str="ball\t paddle\ttimestamp\n"
		pix_str="pixel flash on\n"

		for i in range(len(ball_clone.record)):
			print_str = print_str+repr(ball_clone.record[i])+"\t"+repr(player_clone.record[i])+"\n"

		for rec in pix_record:
			pix_str = pix_str + repr(rec) + "\n"			

		now = datetime.datetime.now()
		filename = now.strftime("%Y-%m-%d-%H-%M")
		pix_filename = now.strftime("%Y-%m-%d-%H-%M") + "_pix"
		print filename, pix_filename
		try:
 			f = open("/Users/Alex/desktop/PONG!/data/"+filename+".txt", "w")
			try:
				f.write(print_str)
			finally:
				f.close()

			f = open("/Users/Alex/desktop/PONG!/data/"+pix_filename+".txt", "w")
			try:
				f.write(pix_str)
			finally:
				f.close()

		except IOError:
			pass
		game_window.close()

def sync_on(dt, record):
	sync_pixel.visible = True
	record.append(time.time())
	pyglet.clock.schedule_once(sync_off, 0.01)

def sync_off(dt):
	sync_pixel.visible = False

	
# Run the code
if __name__ == '__main__':
    # run update 120 time per second
    record = []
    pyglet.clock.schedule_interval(update, 1/200.0, theta, arena, pix_record)
    pyglet.clock.schedule_interval(sync_on, 1, pix_record)
    # run pyglet
    pyglet.app.run()
