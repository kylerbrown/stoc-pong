# PONG.PY 

import pyglet
from game import constants, resources, player, ball, geometry, record

# initialize window
gameWindow = pyglet.window.Window(fullscreen=True,vsync=True)

# get game constants
setGameRadius = 180
values = constants.Constants(gameWindow=gameWindow,radius=setGameRadius)
geom = geometry.Geometry(constants=values)

# initialize batches
mainBatch = pyglet.graphics.Batch()		# the permanent game elements
altBatch = pyglet.graphics.Batch()		#  a holding batch for elements
										#  (not drawn)

# define game elements
# static elements
# initialize paddle path
paddlePath = pyglet.sprite.Sprite(img=resources.path_image,
									x=values.centerX,
									y=values.centerY,
									batch=mainBatch)

paddlePath.scale = values.pathScale
# center marker
centerMark = pyglet.sprite.Sprite(img=resources.marker_image,
									x=values.centerX,
									y=values.centerY,
									batch=mainBatch)
centerMark.scale = values.markerScale

# dynamic elements
# ball
pongBall = ball.Ball(constants=values,geometry=geom,batch=mainBatch)
pongBall.scale = values.ballScale
ballRecord = record.Record(pongBall)		# ball position and time data
# paddle
playerPaddle = player.Player(constants=values,geometry=geom,batch=mainBatch)
playerPaddle.scale = values.paddleScale
paddleRecord = record.Record(playerPaddle)	# paddle position and time data
# synchronization dot
syncDot = pyglet.sprite.Sprite(img=resources.ball_image,
								x=50,
								y=50,
								batch=mainBatch)
syncDot.visible = False
syncRecord = record.Record(syncDot)			# sync dot position and time data

# push key handlers
gameWindow.push_handlers(playerPaddle.key_handler)

# paint screen
@gameWindow.event
def on_draw():
    # clear screen
    gameWindow.clear()
    # draw game elements
    mainBatch.draw()

def update(dt):
	pongBall.update(dt,playerPaddle,values)		# update ball
	playerPaddle.update(dt,values)				# update paddle
	ballRecord.update(dt)						# update ball record
	paddleRecord.update(dt)						# update paddle record
	
# synchronization dot update 
def sync_on(dt):
	#if not (game_flow.in_play == "before"):
	syncDot.visible = True
	syncRecord.update(dt)
		# print record
		# print "\n"
		# increased spot duration to 0.5 s 
	pyglet.clock.schedule_once(sync_off, 0.5)

def sync_off(dt):
	syncDot.visible = False
    
# Run the code
if __name__ == '__main__':
	# schedule the update function at 200 Hz
	pyglet.clock.schedule_interval(update,1/200.0)
	# schedule the sync dot update function for 0.5 Hz
	pyglet.clock.schedule_interval(sync_on,2)
    # run pyglet
	pyglet.app.run()
