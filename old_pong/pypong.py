import pygame, sys

pygame.init()

size = width, height = 620, 480
speed = [1,1]
black = 0, 0, 0
screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

clock = pygame.time.Clock()


for i in range(5000):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0]=-speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    fps = clock.get_fps()
    print(fps)
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    clock.tick()
