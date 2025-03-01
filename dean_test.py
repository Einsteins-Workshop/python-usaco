import pygame
from pygame.draw import*


print('1')
pygame.init()

width=1000
hight=800
game_surface=pygame.display.set_mode((width,hight))
clock=pygame.time.Clock()
FPS=10

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)

running=True

while running==True:
    for event in pygame.event.get():
        # if the event is us closing the game window
        if event.type == pygame.QUIT:
            # stop our loop
            running = False
    mouse_x, mouse_y = pygame.mouse.get_pos()
    print(mouse_x, mouse_y)
    pressed_keys=pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT]:
        running=False
    clock.tick(FPS)
    game_surface.fill(WHITE)
    pygame.display.flip()