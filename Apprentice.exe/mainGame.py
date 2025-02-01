import pygame
import random
from os import path

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

running = True

while running == True:
    clock.tick(FPS)

    #Other stuff
    game_surface.fill(WHITE)

    #Other stuff
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False