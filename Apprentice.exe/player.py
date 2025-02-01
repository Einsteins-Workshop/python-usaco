import pygame
from os import path

class Player(pygame.sprite.Sprite):
    def __init__(self,screen_width, screen_height, color):
        pygame.sprite.Sprite.__init(self)

        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')

        self.player_img = pygame.image.load(path.join(img_folder, "player_image.png")).convert()