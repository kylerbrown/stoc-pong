# RESOURCES.PY - load game resources

import pyglet

# Set location for resources
pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

# Load game images
player_image = pyglet.resource.image("paddle.png")
ball_image = pyglet.resource.image("ball.png")
arena_image = pyglet.resource.image("arena.png")
path_image = pyglet.resource.image("path.png")
marker_image = pyglet.resource.image("marker.png")

# Redefines reference point of the image object to the center of the image
def center_image(image):
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2

center_image(arena_image)
center_image(player_image)
center_image(ball_image)
center_image(path_image)
center_image(marker_image)

