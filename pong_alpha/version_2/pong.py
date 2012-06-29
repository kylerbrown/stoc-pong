# PONG.PY - basic pong game

import pyglet, random, datetime, math
from pyglet.window import key
from game import resources, player, ball, arena, ui
from game import playerclone, ballclone, arenaclone
from pyglet.gl import *

# Initialize window
game_window = pyglet.window.Window(600, 600)

# Initialize batches
main_batch = pyglet.graphics.Batch()
alt_batch = pyglet.graphics.Batch()

# Set theta
theta = 45

# Initialize paddle, ball, and clones as sprites
arena = arena.Arena(batch=main_batch)
arena.visible = False
arena_clone = arenaclone.ArenaClone(batch=main_batch)
arena_clone.rotation = -theta

player_paddle = player.Player(x=300,y=175,batch=main_batch)
player_paddle.visible = False
player_paddle.scale = 0.5
player_clone = playerclone.PlayerClone(batch=main_batch)
player_clone.rotation = -theta
player_clone.scale = 0.5

ball = ball.Ball(batch=main_batch)
ball.visible = False
ball.scale = 0.3
ball_clone = ballclone.BallClone(batch=main_batch)
ball_clone.scale = 0.33

game_flow = ui.UI(batch=main_batch)

# Initialize game objects to a list
game_objects = [player_paddle, ball]

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
    alt_batch.draw()

def update(dt,theta,arena):
	ball.update(dt,arena)
	ball_clone.update(ball,theta,game_window)

	player_paddle.update(dt,arena)
	player_clone.update(player_paddle,theta,game_window)
	
	game_flow.update(dt)

	if ball.collides_with(player_paddle):
		ball.handle_collision(dt)

	ball.in_play = game_flow.in_play

	if game_flow.quit_game:
		print_str="ball \t paddle \n"
		for i in range(len(ball_clone.record)):
			print_str = print_str+repr(ball_clone.record[i])+"\t"+repr(player_clone.record[i])+"\n"
		now = datetime.datetime.now()
		filename = now.strftime("%Y-%m-%d-%H-%M")
		print filename
		try:
 			f = open("/Users/Alex/desktop/PONG!/data/"+filename+".txt", "w")
			try:
				f.write(print_str)
			finally:
				f.close()
		except IOError:
			pass
		game_window.close()

	
# Run the code
if __name__ == '__main__':
    # run update 120 time per second
    pyglet.clock.schedule_interval(update, 1/200.0, theta, arena)
    # run pyglet
    pyglet.app.run()
