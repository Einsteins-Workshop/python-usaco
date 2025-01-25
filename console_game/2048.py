# We will look to recreate the 2048 game.  For a demo of the game, see https://2048game.com/
#
# The game is played in a 4x4 grid of cells, some of which have numbers.  Initially two random cells
# have a 2 in it. The rest of the cells are empty.
#
# Each turn, the player can press keys to move up, down, left, and right.  All cells shift as far
# as they can in that direction.  If two elements with the same number meet, they combine into one
# single cell with their sum.
#
# After the existing elements have been moved as far as they can go, a random empty cell will be filled
# with a 2.
#
# If the player can get 2048 in any cell, they win.  If there are no empty cells to add a new 2, and
# there are no moves that can be performed, the game is over.

# Here is the sample output that we want to have for the game:
#
# Commands are as follows :
# 'W' or 'w' : Move Up
# 'S' or 's' : Move Down
# 'A' or 'a' : Move Left
# 'D' or 'd' : Move Right
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 2, 0]
# Enter a move: a
# GAME NOT OVER
# [0, 0, 0, 2]
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [2, 0, 0, 0]
# Enter a move: s
# GAME NOT OVER
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 2, 0]
# [2, 0, 0, 2]
# Enter a move: d
# GAME NOT OVER
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [2, 0, 0, 2]
# [0, 0, 0, 4]
# Enter a move: a
# GAME NOT OVER
# [0, 2, 0, 0]
# [0, 0, 0, 0]
# [4, 0, 0, 0]
# [4, 0, 0, 0]
# Press the command : s
# GAME NOT OVER
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [8, 2, 0, 2]
# .
# .
# .
# And the series of input output will go on till we lose or win!

# Fill out the logic as follows to complete the game

import random

# Use these constants to represent current state of the game
WIN = 1
LOSS = 2
GAME_NOT_OVER = 3
def print_grid(grid):
    print(grid[0])
    print(grid[1])
    print(grid[2])
    print(grid[3])
    print(grid[2][3])
print_grid([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
def start_game():
    #Create a grid that
    grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    # Print to the user the commands that they can use. The simplest approach
    # is to use w or W for moving up, s or S for moving down, a or A for moving left, and d or D for moving
    # right.
    print(f"Use WASD to move!")
    # Call the method to add a new 2 to the grid
    add_new_2()
    # return the grid
    return grid
def add_new_2(grid):
    # This should add a 2 to a random empty position in the grid. Be sure to check to make
    # sure that the 2 is not added to a cell which already has a number. Although not necessary,
    # it is good coding practice to return the grid
    import random

    return

def check_win_or_loss(grid):
    # TODO: If any cell has 2048, then this should return WIN
    #
    # TODO: If there is at least one empty cell for which to put a 2, this should return
    # GAME_NOT_OVER
    #
    # TODO: If there is a possible move that merges cells, this should return GAME_NOT_OVER.
    # This happens when there are two cells with the same number that are adjacent horizontally or vertically.
    #
    # Otherwise, return lost
    return LOSS

# This method shifts all elements to the left, making sure that there are no empty cells between
# the numbered cells and the left border
def shift_left(grid, changed):
    # TODO: Create a new grid that is empty.
    # ADVANCED TODO: Create a new function for creating a new grid and use it both here and in
    # start_game()
    new_grid = []

    # TODO: For each row, go through each cell in the row and put it in an unused column in that
    # row.  In each row, you'll want to use a temporary variable to keep track of the leftmost unused
    # column as you are shifting the cells. Also, mark that the grid has changed if any elements are not
    # where they started at.

    return new_grid

def merge_left(grid):
    # TODO: For each row, check each pair from left to right.  If they have the same value, double
    # the left cell of the pair and make the cell to the right empty. If any merging happens, make
    # sure to mark changed as True.

    return grid

def reverse(grid):
    new_grid = []
    # TODO: reverse each row of the grid
    return new_grid

def transpose(grid):
    new_grid = []
    # TODO: switch the columns and the rows of the grid, so the cell element in (i,j) should now be in
    # j, i
    return new_grid

def move_left(grid):
    # first we shift the grid
    new_grid, changed_1 = shift_left(grid)
    # then we merge the cells
    new_grid = changed_2 = merge_left(new_grid)

    # then we shift the grid again, if necessary (merging can create gaps)
    new_grid, _unused_changed = shift_left(new_grid)

    return new_grid

def move_right(grid):
    # TODO: to move right, reverse the grid, move_left, and then reverse the grid again
    return grid

def move_up(grid):
    # TODO: to move up, transpose the grid, move_left, and then transpose the grid back
    return grid

def move_down(grid):
    # TODO: to move up, transpose the grid, move_right, and then transpose the grid back
    return grid

# Start by calling the start_game function to get the starting grid
grid = start_game()

# Keep looping to get user input until the game is over
while True:
    user_input = input("Enter a move:")

    # TODO: Check the user input. If it is one of the acceptable move keys, use the appropriate
    # function move_up, move_down, move_left, and move_right.  Otherwise, warn the user that the
    # key was invalid and, optionally, print out again the keys for the possible moves

    # TODO: Using check_win_or_lose, check the state of the game. If the game is not over, use add_new_2
    # to add a new 2 cell. Otherwise, tell the user that the game is over and either break out of loop
    # or exit program.

    # TODO: Print out the current grid by either just using the print function or doing something
    # a bit fancier, see https://stackoverflow.com/questions/8450472/how-to-print-a-string-at-a-fixed-width


