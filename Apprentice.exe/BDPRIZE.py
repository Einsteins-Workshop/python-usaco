import pygame
import random

PRIZE_WIDTH = 25
PRIZE_HEIGHT = 25

class Prize(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PRIZE_WIDTH, PRIZE_HEIGHT))
        self.image.fill(color)

        self.rect = self.image.get_rect()

        self.rect.center = (random.randint(25,screen_width -25),random.randint(25,screen_height - 25))
        self.x_speed = random.randint(-5,5)
        self.y_speed = random.randint(-5,5)

        self.width = screen_width
        self.height = screen_height

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.right >+ self.width:
            self.x_speed *= -1.1
        if self.rect.left <= 0:
            self.x_speed *= -1.1
        if self.rect.bottom >+ self.height:
            self.y_speed = -1.1*abs(self.y_speed)
        if self.rect.top <= 0:
            self.y_speed = 1.1*abs(self.y_speed)