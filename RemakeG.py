import pygame
import random

pygame.init()
width = 600
height = 400
game_surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('HOI')
clock = pygame.time.Clock()
FPS = 60

NOTWHITE = (0,255,200)
BLACK = (0,0,0)
OTHERCOLOR = (0,55,66)

player_x = 300
player_y = 300
player_size = 25
speed = 10

prizeBox_x = random.randint(50,width - 50)
prizeBox_y = random.randint(50,height - 50)
prizeBox_size = 10
prizeBox_speed = random.randint(3,7)

running = True

while running== True:
    clock.tick(FPS)
    #Draw stuff

    game_surface.fill(NOTWHITE)
    pygame.draw.rect(game_surface, BLACK, pygame.Rect(player_x, player_y, player_size, player_size))
    pygame.draw.rect(game_surface, OTHERCOLOR, (prizeBox_x, prizeBox_y, prizeBox_size,prizeBox_size))
    #Inputs

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT]:
        player_x -= speed
    if pressed_keys[pygame.K_RIGHT]:
        player_x += speed
    if pressed_keys[pygame.K_UP]:
        player_y -= speed
    if pressed_keys[pygame.K_DOWN]:
        player_y += speed
    if player_x <= 0:
        player_x = 0
    if player_x + player_size >= width:
        player_x = width - player_size
    if player_y <= 0:
        player_y = 0
    if player_y + player_size >= height:
        player_y = height - player_size
    #NonInputs

    prizeBox_x += prizeBox_speed
    if prizeBox_x + prizeBox_size >= width or prizeBox_x <= 0:
        prizeBox_speed *= -1
        prizeBox_x += prizeBox_speed

    pygame.display.flip() #UpdateFrames

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
