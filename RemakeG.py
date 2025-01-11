import pygame

pygame.init()
width = 1200
height = 800
game_surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('HOI')
clock =pygame.time.Clock()
FPS = 60

NOTWHITE = (0,255,200)
BLACK = (0,0,0)

player_x = 100
player_y = 100
player_size = 30
speed = 15



running = True

while running== True:
    clock.tick(FPS)
    game_surface.fill(NOTWHITE)
    pygame.draw.rect(game_surface, BLACK, pygame.Rect(player_x, player_y, player_size, player_size))
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT]:
        player_x -= speed
    if pressed_keys[pygame.K_RIGHT]:
        player_x += speed
    if pressed_keys[pygame.K_UP]:
        player_y -= speed
    if pressed_keys[pygame.K_DOWN]:
        player_y += speed

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
