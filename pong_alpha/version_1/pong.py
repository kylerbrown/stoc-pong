# PONG.PY - basic pong game
# matt battifarano

## LOAD MODULES
import pyglet, random, datetime
from pyglet.window import key
from game import resources, player, ball
##

## INITIALIZE GAME ELEMENTS
# Initialize window
game_window = pyglet.window.Window(800, 600)
# Initialize batches
main_batch = pyglet.graphics.Batch()
alt_batch = pyglet.graphics.Batch()
# Initialize game orientation (angle of paddle with horizantal)
orientation = 0
# Initialize text labels
score_label = pyglet.text.Label(text="Score: 0",
								x=10,y=575, batch=alt_batch)
level_label = pyglet.text.Label(text="Pong!", 
                                x=400, y=575,anchor_x='center',batch=alt_batch)
# Initialize paddle and ball as sprites
player_paddle = player.Player(batch=main_batch)
ball = ball.Ball(batch=main_batch)
# Initialize game objects to a list
game_objects = [player_paddle, ball]
# Push key handler
game_window.push_handlers(player_paddle.key_handler)
game_window.push_handlers(ball.key_handler)
##

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
	if ball.quit_game:
		print_str="ball \t paddle \n"
		for i in range(len(ball.record)):
			print_str = print_str+repr(ball.record[i])+"\t"+repr(player_paddle.record[i])+"\n" 
		print print_str
		now = datetime.datetime.now()
		filename = now.strftime("%Y-%m-%d-%H-%M")
		print filename
		try:
			f = open("Coding/Python/pong_alpha/data/"+filename+".txt", "w")
			try:
				f.write(print_str) 
			finally:
				f.close()
		except IOError:
			pass
		game_window.close()

# Tell pyglet to run the code
if __name__ == '__main__':
    # run update 120 time per second
    pyglet.clock.schedule_interval(update, 1/200.0)
    # run pyglet
    pyglet.app.run()
##