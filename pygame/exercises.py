# This document outlines the steps required to create a pygame exercise to show how to
# have a player-controlled object that can move, chasing an automatically moving bonus object.
# We will in a later exercise built towards creating the game in
# https://github.com/Einsteins-Workshop/pygame-dodger.

# The exercises start with pygame/main.py, and each step adds a part of the sample game.
# You are encouraged to use your own embellishments to the steps mentioned below.

# The following can be ignored, they are to set up variables that are used in code snippets
import pygame
game_surface =  pygame.display.set_mode((100, 100))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Step 1:
# Copy main.py to your own file and try running the program.  Make sure that pygame
# is installed for python (you can use the command 'pip -m install pygame' in your operating
# system command prompt). Notice that a window appears. As you move the mouse within the pygame
# window, the console will print out the coordinates of the mouse.
#
# Note that the top left starts at 0,0 and the bottom right has coordinates equal to the width
# and height variables defined in the top of the program and passed to the pygame.display.set_mode
# method.
#
# Step 2:
# Look at the BLACK, WHITE, RED, and GREEN constants. They represent RGB values.
# a) Try looking up information on RGB values.
# b) Try changing the background to RED or GREEN.
# Try creating a custom color for the background, like BLUE.
#
# Step 3:
# Notice that there is a caption for the game. The original program we called had a generic
# 'Window Caption!' name.  Find in the program where that is set and add your own name.
#
# Step 4:
# Draw a player square. Drawing an image is a bit more complicated than you would expect.
# a) Define parameters for player_x (player x position), player_y (player y position) and
#    player_size (the number of pixels that the player should be.  The parameters should be
#    before the loop, I recommend putting it after the section that sets up the game resources
#    such as colors. Here are some recommended starting values:
player_x = 100
player_y = 100
player_size = 10
# b) In the draw stuff section, draw the square.  Use the pygame.draw.rect function.  Below
#    is a sample function that calls the method.  Note that pygame.draw.rect takes three somewhat
#    complicated parameters: a surface (defined as game_surface in main.py), a color, and a
#    pygame rectangle, which itself is defined by four parameters: an x position, a y position,
#    the width (in pixels) and the height (also in pixels).
pygame.draw.rect(game_surface, BLACK, pygame.Rect(player_x, player_y, player_size, player_size))

# Step 5: Move the player square.  We will allow the player to use the keyboard left, right, up
#  and down keys to move the square in the direction pressed.
#  a) Initialize the speed function.  In the same section that you se the other player variables,
#    set up the speed variable
speed = 5

#   b) In the update stuff section of the main loop, check if the player pressed the left arrow or
#     right arrow and move the player by the speed by changing player_x, the player's x position.
#     See https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed for more info about key
#     buttons
pressed_keys = pygame.key.get_pressed()
if pressed_keys[pygame.K_LEFT]:
    player_x -= speed
if pressed_keys[pygame.K_RIGHT]:
    player_x += speed
#   c) Similarly, add the ability to move up and down, using the pygame.K_UP and pygame.K_DOWN keys,
#      and using that to change the player_y variable.
#
#   d) As an experiment, instead of the buttons moving the player directly, have them accelerate the
#      player instead.

#      In initialization section:
player_x_speed = 5
player_acceleration = 2
#      In update stuff section
pressed_keys = pygame.key.get_pressed()
if pressed_keys[pygame.K_LEFT]:
    player_x -= player_x_speed
    player_x_speed += player_acceleration
elif pressed_keys[pygame.K_RIGHT]:
    player_x += player_x_speed
    player_x_speed += player_acceleration
else:
    player_x_speed = 5

#   e) Try adding a similar clause for vertical movement, using a player_y_speed variable to change
#      the player_x position.

# Step 6: Respecting the boundary
# Currently, the player can go off the screen. We want to make sure that this does not happen, as
# that would effectively make the character invisible to the player. As such, we will enforce
# the boundary so that the player cannot go off screen.
#
# a) Keep the player within the width of the screen
#    As the last part of the update stuff section:
width = 1000
if player_x <= 0:
    player_x = 0
# We want to make sure that all of the character is within the screen. Given that we have player_x
# represent the left-most part of the character, we have to make sure to adjust the right hand
# check to include the player_size to incorporate the right-most part of the character.
if player_x + player_size >= width:
    player_x = width - player_size
#
# b) Add boundary checking for top and bottom of the window.
#
# Step 7: Create a randomly moving reward
# a) Similar to the player, set up variables for the bonus object. Make sure to make the color of
#    the bonus object is different from the player

#    In variable setup section:
bonus_x = 500
bonus_y = 500
bonus_size = 10
bonus_x_speed = 3
bonus_y_speed = 2
#    In draw stuff section:
pygame.draw.rect(game_surface, RED, (bonus_x, bonus_y, bonus_size, bonus_size))

# b) Have the bonus object keep moving until it heads the edge of screen, and then bounce

#    In update stuff section:
bonus_x += bonus_x_speed
# If the bonus hits the right side, reverse the horizontal direction of the reward
if (bonus_x + bonus_size >= width):
    bonus_x_speed *= -1
# Move it a second time, to make sure it bounces back into display area
bonus_x += bonus_x_speed

# c) Add a boundary check to the left, so that the bonus object's horizontal position cannot be
#    negative

# d) Add the ability of the bonus object to move diagonally by independently changing the y-axis
#    value

# e) Have the bonus object start at a random position within the width and height of the screen
#
# f) Have the starting x and y speeds be random, within a fixed range of 1 to 5 for each


