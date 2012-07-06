# PONG.PY 

import pyglet
from game import resources, player, ball

# initialize window
gameWindow = pyglet.window.Window(fullscreen=True, vsync=True)

# initialize batches
mainBatch = pyglet.graphics.Batch()		# the permanent game elements
altBatch = pyglet.graphics.Batch()		# a holding batch for elements
										# (not drawn)

# screen position constants
centerX = 0.5 * gameWindow.width
centerY = 0.5 * gameWindow.height
gameRadius = 180
pathWidth = 2.5			# the width in pixels of the path in path.png

# initialize paddle path
paddlePath = pyglet.sprite.Sprite(img=resources.path_image,
									x=centerX,
									y=centerY,
									batch=mainBatch)
pathRadius = 0.5 * paddlePath.width
pathScale = gameRadius/pathRadius
paddlePath.scale = pathScale

# define game elements
# ball
pongBall = ball.Ball(x=centerX,
						y=centerY,
						batch=mainBatch)
pongBall.scale = 0.3
# paddle
yPos = centerY-gameRadius*(1-(pathWidth/pathRadius))
playerPaddle = player.Player(originX=centerX,
								originY=centerY,
								x=centerX,
								y=yPos,
								batch=mainBatch)
playerPaddle.scale = 0.5
# center marker
centerMark = pyglet.sprite.Sprite(img=resources.marker_image,
									x=centerX,
									y=centerY,
									batch=mainBatch)
centerMark.scale=.06

# push key handlers
gameWindow.push_handlers(playerPaddle.key_handler)

# Paint screen
@gameWindow.event
def on_draw():
    # clear screen
    gameWindow.clear()
    # draw game elements
    mainBatch.draw()

def update(dt):
	playerPaddle.update(dt)
	pongBall.update(dt)
    
# Run the code
if __name__ == '__main__':
	# schedule the update function
	pyglet.clock.schedule_interval(update,1/200.0)
    # run pyglet
	pyglet.app.run()
