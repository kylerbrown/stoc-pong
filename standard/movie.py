import pyglet, time, sys
from game import resources, player, ball, arena

filename = "../data/" + sys.argv[1] + ".txt"
f = open(filename)
data = f.readlines()
f.close()

# Initalize global variables
global ball_coords
ball_coords = []
global paddle_coords 
paddle_coords = []
global eye_coors
eye_coords = []
global count
count = 0

# Extract data
for line in data:
	line = line.strip("\n")
	line = line.split("\t")
	ball_coords.append([float(line[0]),float(line[1])])
	paddle_coords.append([float(line[2]),float(line[3])])
	eye_coords.append([float(line[4]),float(line[5])])

game_window = pyglet.window.Window(fullscreen=True,vsync=True)
center_x = 512
center_y = 384

main_batch = pyglet.graphics.Batch()

theta = int(sys.argv[2])

# Initialize sprites
arena = arena.Arena(x=center_x,y=center_y,batch=main_batch)
arena.rotation = -theta
paddle = player.Player(batch=main_batch)
paddle.scale = 0.5
paddle.rotation = -theta
eye = ball.Ball(x=center_x,y=center_y,batch=main_batch)
eye.scale = 0.1
ball = ball.Ball(x=center_x,y=center_y,batch=main_batch)
ball.scale = 0.3
ball.rotation = -theta

# Paint screen
@game_window.event
def on_draw():
	game_window.clear()
	main_batch.draw()

# Update
def update(dt):

	print dt 
	global ball_coords
	global eye_coords
	global paddle_coords
	global count

	ball.x = ball_coords[count][0]
	ball.y = ball_coords[count][1]
	paddle.x = paddle_coords[count][0]
	paddle.y = paddle_coords[count][1]
	eye.x = eye_coords[count][0] + center_x
	eye.y = eye_coords[count][1] + center_y
	eye.color = (255,0,0)

	count = count + 2

# Run
if __name__ == '__main__':
	pyglet.clock.schedule_interval(update, 1/500.0)
	pyglet.app.run()

	