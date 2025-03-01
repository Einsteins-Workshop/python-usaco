import pygame
import random
from os import path
from player import Player
from BDPRIZE import Prize

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
all_prizes = pygame.sprite.Group()
prize = Prize(width, height, RED)
all_sprites.add(prize)
all_prizes.add(prize)
prizes_on_screen = 1

running = True

while running == True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT]:
        player.move_left()
    if pressed_keys[pygame.K_RIGHT]:
        player.move_right()
    if pressed_keys[pygame.K_UP]:
        player.move_up()
    if pressed_keys[pygame.K_DOWN]:
        player.move_down()
    hits = pygame.sprite.groupcollide(all_prizes, all_players, True, False)
    for prize in hits:
        prizes_on_screen -= 1
    if prizes_on_screen == 0:
        prize = Prize(width, height, RED)
        all_sprites.add(prize)
        all_prizes.add(prize)
        prizes_on_screen = 1
    all_sprites.update()
    #Draw
    game_surface.fill(WHITE)
    all_sprites.draw(game_surface)

    pygame.display.flip()
    #Other stuff