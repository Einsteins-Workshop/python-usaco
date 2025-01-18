# First, we want to keep track of the current player, the turn, and the board.  I recomment storing the
# board as a list of nine elements, each keeping track of one of the positions in the 3x3 board
player = "X"
current_board = [] # This should be initialized with nine values represent the symbol to choose that square
turn = 0

# Define a function that prints the board
def print_board(board):
    # This should print the nine board positions with the current value in board
    pass

# Loop until there is a winner or the turn is 9 and all positions have been filled in
    # Print the current board state
    print_board(current_board)

    # Ask the current player to choose a square.  Fill in the board at that position with the player's
    # symbol

    # Check to see if there are is a winner by checking all eight possible three in a row options. If
    # there is a three in a row, declare that player the winner and exit the program

# If turn 9 is passed, declare the game a draw