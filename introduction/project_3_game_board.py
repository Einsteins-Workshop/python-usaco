# We are going to print a tic-tac-toe board
# First, store the board state in a list

# Extend the board to contain nine squares
board = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Print the board three elements at a time.
#print(board[0], "|", board[1], "|", board[2],)
# Continue printing the rest of the board
print(board[0], "|", board[1], "|", board[2],)
print(board[3], "|", board[4], "|", board[5],)
print(board[6], "|", board[7], "|", board[8])
# Ask the user for a square
square = input("Tell me a number on one of the squares shown.")
# Replace the appropriate part of the board list with an "X"
trusquare = int(square)
board[trusquare] = "X"
#Print the board again with the new X.
print(board[0], "|", board[1], "|", board[2],)
print(board[3], "|", board[4], "|", board[5],)
print(board[6], "|", board[7], "|", board[8])
