# In this game, the computer will set up a multi-digit number, and the player will try to guess the
# number. After each guess, the computer will reveal how many digits were exactly correct and how many
# digits in the number but are not in the correct position.

# Import the random module, see https://www.geeksforgeeks.org/python-random-function/ for more info.
# Alternatively, you can use the "from random import randint" to just get random.

# We define a constant
DIGITS = 5
class MastermindGame():
    def __init__(self, digits):
        # A parameter to check if a guess complets the game.
        self._complete = False
        # Create the hidden number, based on the number of digits

    # Return True if the game is complete, False otherwise
    def is_complete(self):
        pass

    def guess(self, guess):
        # Check to make sure that the guess has the correct number of digits
        correct = 0
        incorrect = 0

        # Check to see if the guess is exactly correct, and set the game to complete if the player
        # guesses the hidden number

        # Find how many digits in the guess are in the correct position. You can loop over all the digits
        # to check

        # Figure out how many digits in the guess are in the hidden number. You can do this by looping
        # over all the digits from 0 - 9, see how many of those are in the hidden number, how many of those
        # are in the guess, and take the lesser of these two quantities.

        # The incorrect position numbers should be the different between the number of common digits in the
        # previous step and the number of digits in the correct position

        return correct, incorrect

quit_playing = False
current_game = None
while True: # Change this loop so that we stop playing if the player quits
    pass
    # If there is no game or the game is complete, create a new game.

    # Ask the player for a guess.

    # Call the guess() function for the game and print out to the user the response of how many
    # digits are in the right position and how many digits are in the hidden number but in the
    # incorrect position.

    # If the game is complete, ask the player if they want to play again