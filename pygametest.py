import pygame
from pygame.draw import*


print('1')
pygame.init()

width=1000
hight=800
game_surface=pygame.display.set_mode((width,hight))
clock=pygame.time.Clock()
FPS=30

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)

running=True

while running==True:
    clock.tick(FPS)
    game_surface.fill(RED)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    print(mouse_x, mouse_y)
    pressed_keys=pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT]:
        running=False
    pygame.display.flip()