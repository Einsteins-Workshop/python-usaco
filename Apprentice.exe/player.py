import pygame
from os import path


class Player(pygame.sprite.Sprite):
    def __init__(self,screen_width, screen_height, color):
        pygame.sprite.Sprite.__init__(self)

        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'IGN')

        self.player_img = pygame.image.load(path.join(img_folder, "player_image.png")).convert()
        self.image = pygame.transform.scale(self.player_img, (50,50))
        self.image.set_colorkey(color)

        self.rect = self.image.get_rect()
        self.rect.center = (10,10)

        self.x_speed = 6
        self.y_speed = 6

        self.width = screen_width
        self.height = screen_height

    def update(self):
        if self.rect.right >= self.width:
            self.rect.right = self.width -1
        if self.rect.left <= 0:
            self.rect.left = 1
        if self.rect.bottom >= self.height:
            self.rect.bottom = self.height -1
        if self.rect.top <= 0:
            self.rect.top = 1

    def move_left(self):
        self.rect.x -= self.x_speed

    def move_right(self):
        self.rect.x += self.x_speed

    def move_up(self):
        self.rect.y -= self.y_speed

    def move_down(self):
        self.rect.y += self.y_speed
