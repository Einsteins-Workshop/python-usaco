# This document outlines the steps required to create the game in
# https://github.com/Einsteins-Workshop/pygame-dodger. I suggest you create a new directory
# to store the files for this game, and you can if you wish start with the work that you
# have done in exercises.py, though many sections of that will be removed. The instructions
# will assume that you are starting afresh, with annotations made for sections that are
# repeated or are very similar to that in exercises.py

# The exercises start with pygame/main.py, and each step adds a part of the sample game.
# You are encouraged to use your own embellishments to the steps mentioned below. Also,
# you should run your program, as you develop it, often in order to test your code.

# The following can be ignored, they are to set up variables that are used in code snippets
import pygame
import random
from os import path

# The game window width and height.  When making your game, you should alter these to
# best fit within your screen
width = 1200
height = 800

# RGB values for colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Purely to make code snippets not error
game_surface =  pygame.display.set_mode((100, 100))

# Step 1: (Repeat of exercises.py Step 1)
# Copy main.py to your own file and try running the program.  Make sure that pygame
# is installed for python (you can use the command 'pip -m install pygame' in your operating
# system command prompt). Notice that a window appears. As you move the mouse within the pygame
# window, the console will print out the coordinates of the mouse.
#
# Note that the top left starts at 0,0 and the bottom right has coordinates equal to the width
# and height variables defined in the top of the program and passed to the pygame.display.set_mode
# method.

# Step 2: (Repeat of exercises.py Step 3)
# Notice that there is a caption for the game. The original program we called had a generic
# 'Window Caption!' name.  Find in the program where that is set and add your own name.

# Step 3: In your game directory, create a new file called player.py. A lot of pygame
# specific code will be specified

# Note that this class will inherit from pygame's Sprite class, and so will have
# for free its image and its collision detection methods.

# Make sure to import both pygame and path
# import pygame
# from os import path
class Player(pygame.sprite.Sprite):
    # The following method is what will be called when we create a new player object
    def __init__(self, screen_width, screen_height, color):
        # We will be calling the inherited Sprite's initialization function, which are
        # required for some of the inherited methods.
        pygame.sprite.Sprite.__init(self)

        # Define how it works, first set up folders with sprite images and the game
        # This is a bit magic, it gets the folder that the current file is in
        game_folder = path.dirname(__file__)
        # The following assumes that the image folder is in your game directory
        # if not, you may want to specify this directly (by hard coding it) or you
        # can move the image directory to your game directory
        img_folder = path.join(game_folder, "img")

        # The following is pygame's image processing
        # use image from img directory as player. You can experminet with other .png
        # files if you wish
        self.player_img = pygame.image.load(path.join(img_folder, "player_image.png")).convert()
        self.image = pygame.transform.scale(self.player_img, (50, 50))
        self.image.set_colorkey(color)

        # Set bounding box for collisions based on image size
        # We can define the rectangle based on its center rather than specifying
        # its top, bottom, left and right attributes
        self.rect = self.image.get_rect()
        self.rect.center = (10, 10)

        # set the initial position and speed
        self.rect.center = (10, 10)
        self.x_speed = 0 # Change this to some value
        self.y_speed = 0 # Change this to some value

        # save screen sizes for boundary checks
        self.width = screen_width
        self.height = screen_height

    # This method is actually a function that is expected to be overwritten by all
    # classes that inherits Sprite, and is used for all changes that must be checked
    # during each frame of the animation. Note that this won't include explicit
    # user inputs
    def update(self):
        # Make sure that the player stays on screen during update, note that you can
        # check and manipuate the rect attribute of the player sprite, which will move it
        # on the screen
        # Similar to exercises.py Step 6
        if self.rect.right >= self.width:
            self.rect.right = self.width - 1
        if self.rect.left <= 0:
            self.rect.left = 1
        # Put in update checks for self.rect.top, and self.rect.bottom here

    # Define player movement functions
    def move_left(self):
        self.rect.x -= self.x_speed
    def move_right(self):
        self.rect.x += self.x_speed
    def move_up(self):
        pass # You should define this
    def move_down(self):
        pass # You should define this

# Step 4: Adding our player to the game.  All of these changes should be in your main
# game file

# In import section, we need to link in our new Player class so that our game knows about it
# You will add something like:
# from player import Player

# In the setup game resources section, set up our sprite groups. These will work
# like lists. Also create our player and add it to groups
all_players = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player = Player(width, height, BLACK)
all_sprites.add(player)
all_players.add(player)

# In the event updates section, add event handling for keyboard inputs
pressed_keys = pygame.key.get_pressed()
if pressed_keys[pygame.K_LEFT]:
    player.move_left()
# Add similar checks for moving up, down, left and right

# In update stuff section, make sure to have sprites update for boundary checks
all_sprites.update()

# In draw stuff section, makes sure to draw sprites
all_sprites.draw(game_surface)

# Step 5: Creating prize object. This should be called prize.py (although it is called
# enemy.py in python-dodger project)
# Make sure to import pygame and random
# import pygame
# import random

# Initialize prize width and height
PRIZE_WIDTH = 25
PRIZE_HEIGHT = 25

# Inherits all properties of the Sprite object
class Prize(pygame.sprite.Sprite):
    # This is run on the creation of each object
    def __init__(self, screen_width, screen_height, color):
        pygame.sprite.Sprite.__init__(self)
        # define how it looks, for now just a block of color
        self.image = pygame.Surface((PRIZE_WIDTH, PRIZE_HEIGHT))
        self.image.fill(color)

        # set bounding box for collisions based on image size
        # the rect has top, bottom, left, and right which has position
        self.rect = self.image.get_rect()

        # set initial position and speed
        self.rect.center = (250, 250) # Change this to be a random place within screen height
                                    # and width, and possibly not within 50 pixles of edge
        self.x_speed = random.randint(2, 6)
        self.y_speed = random.randint(2, 6)

        # Save screen sizes for boundary checks
        self.width = screen_width
        self.height = screen_height
    def update(self):
        # Move the object along its path
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # Have the object bounce if it hits the boundary
        if self.rect.right >= self.width:
            self.x_speed *= -1
        if self.rect.left <= 0:
            self.x_speed *= -1
        # Put update checks for self.rect.top and self.rect.bottom here

# Step 6: Add prize to main file

# In import section make sure to reference prize
# from prize import Prize

# In the setup game resources section, add prize object and sprite group for prize
all_prizes = pygame.sprite.Group()
prize = Prize(width, height, RED)
all_sprites.add(prize)
all_prizes.add(prize)
prizes_on_screen = 1

# In update stuff section, check for collisions, which will destroy prizes if they are
# touched
hits = pygame.sprite.groupcollide(all_prizes, all_players, True, False)
# Keeping track of how many sprites still exist
for prize in hits:
    prizes_on_screen -= 1

# Step 7: Introduce scoreboard

# In setup game resources, add score and font for scoreboard
score = 0
font = pygame.font.Font(None, 36)

# In draw stuff section after drawing all sprites but before update display with pygame.display.flip()
text = font.render("Score: " + score.__str__(), True, BLACK)
game_surface.blit(text, (50,50))

# Step 8: Introduce stages, where we add progressively more prizes after all prizes have
# been collected

# In the setup game resources section
stage = 1

# After all prize collisions are checked, see if we need to update the prizes
if False: # change to check that there are no more prizes on the screen. You can use
        # the prizes_on_screen variable for that check
    stage = 1 # Change to add one to the stage
    # Add prizes
    for x in range(1): # Change to add a number of prizes equal to the new stage
        new_prize = Prize(width, height, RED)
        all_sprites.add(new_prize)
        all_prizes.add(new_prize)
    prizes_on_screen = 1 # Change to se to the number of prizes actually added

# Try playing the game now to see how stages work
# You can if you wish change the color of the prizes or have them randomly selected
# among a color pool or by using random RGB values

# Stage 9: Creating enemy (dangerous) objects. This should be put in a new file called enemy.py
#
# Add the following imports to the new file
# import pygame
# import random

# Some constant imports that you can experiment with for ideal size for enemies.
ENEMY_WIDTH = 25
ENEMY_HEIGHT = 25

# Inherits all properties of the Sprite object
class Enemy(pygame.sprite.Sprite):
    # This is run on creation of each enemy object
    def __init__(self, screen_width, screen_height, color):
        # Run the inherited class Sprite's initialization methods, required to get sprites to work.
        pygame.sprite.Sprite.__init__(self)
        # define how it looks, as a rectangle and get its bounding rectangle in order to set its position
        self.image = pygame.Surface((ENEMY_WIDTH, ENEMY_HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect()

        # Set initial position and speed, starting with it above the screen.  Change this so that
        # it starts at a random x position, and consider whether to make it not too close to the corners:
        # one suggestion would be within the pixel x range of 50 to screen_width - 50. Another option
        # is to allow it to touch the corners, but makes sure that the center is then within a range
        # of width/2 and screen_width - width/2 so that the whole image is on the screen.
        # You can use random.randint (See https://www.w3schools.com/python/ref_random_randint.asp)
        # for more info.
        self.rect.center = (100, -10) # Change 100 to random number

        # Setting the speed so they just go down vertically. You should adjust with random speeds,
        # recommendation is a random integer from 2 to 6
        self.x_speed = 0
        self.y_speed = 4 # Change to random number

    # This is called when the sprite group that it is a part of has its update function called
    def update(self):
        # Move the enemy along its path by moving from the top of the screen until it leaves at the
        # bottom of th screen
        if self.rect.top > self.height:
            self.rec.bottom = -10 # Move the object to the start, this should be changed to
                    # reset the center position instead randomly and reset the speed, in a similar
                    # way to the __init__ step.  You can also create a function to get these values
                    # and reuse it for both setting it here and for __init__

# Step 10: Add the enemy obstacles to the main file

# In the import section, add
# from enemy import Enemy

# In the setup game resources section, add a new enemies sprite group
all_enemies = pygame.sprite.Group()

# In the collistion checking section, eliminate the player if they ever touch an enemy
pygame.sprite.groupcollide(all_enemies, all_players, False, True)

# In the section that adds stages, add the following after prizes are created. so that a new enemy
# is added whenever the player goes to the next stage
if (prizes_on_screen == 0):
    # Here would be all the code that adds a new prize

    new_enemy = Enemy(width, height, BLUE) # Create a random color instead, with all RGB values
            # in the range of 100 to 255
    all_sprites.add(new_enemy)
    all_enemies.add(new_enemy)

# Step 11 introduce sound and background
# In import section
#from os import path

# In the setup section, setup game and sound folders.
game_folder = path.dirname(__file__) # Either copy files or set to look in original directories
sound_folder = path.join(game_folder, "sound")
img_folder = path.join(game_folder, "img")


pygame.mixer.music.load(path.join(sound_folder, "lights.wav")) # set game music
collide_sound = pygame.mixer.Sound(path.join(sound_folder, "burp.wav")) # set game sound effect
pygame.mixer.music.play(-1) # start game music and loop indefinitely (-1)

# setup background image
background_image = pygame.image.load(path.join(img_folder, "background.png")).convert()
# scale background image to the size of the screen
background_image = pygame.transform.scale(background_image, (width, height))

# In collision detection section whenever player hits something,  play collide sound
pygame.mixer.Sound.play(collide_sound)

# In drawing section, show background
game_surface.blit(background_image,[0,0])

