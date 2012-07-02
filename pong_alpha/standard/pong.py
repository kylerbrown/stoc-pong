# PONG.PY - basic pong game

import pyglet, random, datetime, math, time
from pyglet.window import key
from game import resources, player, ball, arena, ui
from game import clone
from pyglet.gl import *
import sys

# Initialize window
game_window = pyglet.window.Window(fullscreen=True)
center_x = game_window.width/2
center_y = game_window.height/2

# Initialize batches
main_batch = pyglet.graphics.Batch()
cal_batch = pyglet.graphics.Batch()

# Set theta
theta = int(sys.argv[1])

## Initialize paddle, ball, and clones as sprites
# Arena
arena = arena.Arena(x=center_x,y=center_y,batch=main_batch)
arena.visible = False
arena_clone = clone.Clone(img=resources.arena_image,x=center_x,y=center_y,batch=main_batch)
arena_clone.rotation = -theta
arena_clone.visible = False

print arena.width, arena.image.width
print arena.height, arena.image.height

# Paddle
paddle_scale = 0.5
player_paddle = player.Player(x=center_x,y=(center_y-125),batch=main_batch)
player_paddle.visible = False
player_paddle.scale = paddle_scale
player_clone = clone.Clone(img=resources.player_image,batch=main_batch)
player_clone.rotation = -theta
player_clone.scale = paddle_scale

# Synchronization pixel
sync_pixel = ball.Ball(batch=main_batch)
sync_pixel.visible = False
sync_pixel.scale = 0.2
sync_pixel.x = 20
sync_pixel.y = 20
global pix_record
pix_record = []

# Calibration dots
dot1 = ball.Ball(x=center_x+150,y=center_y,batch=cal_batch)
dot2 = ball.Ball(x=center_x,y=center_y-150,batch=cal_batch)
dot3 = ball.Ball(x=center_x-150,y=center_y,batch=cal_batch)
dot4 = ball.Ball(x=center_x,y=center_y+150,batch=cal_batch)
dots = [dot1, dot2, dot3, dot4]
for dot in dots:
	dot.scale = 0.3

# Ball
ball_scale = 0.3
ball = ball.Ball(x=center_x,y=center_y,batch=main_batch)
ball.visible = False
ball.scale = ball_scale
ball_clone = clone.Clone(img=resources.ball_image,batch=main_batch)
ball_clone.scale = ball_scale

# Game Flow
game_flow = ui.UI(game_window,batch=main_batch)

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
    cal_batch.draw()

def update(dt,theta,arena,pix_record):
	ball.update(dt,arena,game_window)
	ball_clone.update(ball,theta,game_window)

	player_paddle.update(dt,arena)
	player_clone.update(player_paddle,theta,game_window)
	
	game_flow.update(dt)

	if ball.collides_with(player_paddle):
		ball.handle_collision(dt)

	ball.in_play = game_flow.in_play

	if ball.in_play == True:
		arena_clone.visible = True
		player_clone.visible = True
		for dot in dots:
			dot.visible = False
	else:
		arena_clone.visible = False
		player_clone.visible = False
		for dot in dots:
			dot.visible = True

	if game_flow.quit_game:
		print_str="ball\t paddle\ttimestamp\n"
		pix_str="pixel flash on\n"

		for i in range(len(ball_clone.record)):
			print_str = print_str+repr(ball_clone.record[i])+"\t"+repr(player_clone.record[i])+"\n"

		for rec in pix_record:
			pix_str = pix_str + repr(rec) + "\n"			

		now = datetime.datetime.now()
		filename = sys.argv[2]
		print filename
		try:
 			f = open("../data/"+filename+".txt", "w")
			try:
				f.write(print_str)
			finally:
				f.close()

			f = open("../data/"+filename+"_sync.txt", "w")
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
