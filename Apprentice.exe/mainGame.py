import pygame
import random
from os import path
from player import Player

pygame.init()
width = 600
height = 400
game_surface = pygame.display.set_mode((width,height))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
FPS = 60

#Color
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#Other
all_players = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player = Player(width, height, BLACK)
all_sprites.add(player)
all_players.add(player)

running = True

while running == True:
    clock.tick(FPS)
    all_sprites.update()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT]:
        player.move_left()
    if pressed_keys[pygame.K_RIGHT]:
        player.move_right()
    if pressed_keys[pygame.K_UP]:
        player.move_up()
    if pressed_keys[pygame.K_DOWN]:
        player.move_down()


    #Draw
    game_surface.fill(WHITE)
    all_sprites.draw(game_surface)

    pygame.display.flip()
    #Other stuff
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False