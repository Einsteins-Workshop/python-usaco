from rich.console import Console
from rich.theme import Theme
from string import ascii_letters

console = Console(width=40, theme=Theme({"warning": "red on yellow"}))

CORRECT_LETTER = 1
LETTER_IN_WORD = 2
LETTER_NOT_IN_WORD = 3
NOT_LETTER = 4

def main():
    word = get_random_word()

    # TODO: Define a constant with maximum number of guesses, and create an array with that number
    # of guesses with all underlines instead of the one in curreng guesses
    guesses = ["_____"]

    try:
        # TODO: Define a constant with maximum number of guesses, and loop idx for the number of times
        # of the guesses to get a word
        idx = 0
        print_title("Guess 1")
        show_guesses(guesses, word)
        guesses[idx] = guess_word(guesses)

    # If the user exits the program with control-C, skip the error and go to game over.
    except KeyboardInterrupt:
        pass

def get_random_word():
    # TODO:
    # The guessable words are in the guess_words.txt file.  Read the file in and select a
    # random word from the file.
    return "shady"

def show_guesses(guesses, word):
    for guess in guesses:
        # TODO replace the print below with console printing
        print(guess)
        #for letter, correct in zip(guess, word):
        #   TODO: compare letter (the letter in guess) to correct (the correct letter), and if not the
        #       same, see if letter is in the word.  Use console_guess_styling to get the correct status
        #   style = console_guess_styling(__APPROPRIATE_STATUS__)
        #   letter_to_print = f"[{style}]{letter}[/]"
        #   TODO: Keep track, for all guesses (so outside of the guesses loop) of what letters have
        #       been guessed.  Make sure to keep the most accurate value for the letter
        #   console.print("".join(styled_guess), justify="center")
    # Print out all letter statuses

def console_guess_styling(status):
    style = "dim"
    if status == CORRECT_LETTER:
        style = "bold white on green"
    elif status == LETTER_IN_WORD:
        style = "bold white on yellow"
    elif status == LETTER_NOT_IN_WORD:
        style = "white on #666666"
    return style

def guess_word(previous_guesses):
    # TODO: standardize letters to upper case
    # TODO: replace with console version
    guess = input("\nGuess word: ")
    #guess = console.input()

    # TODO: Check to make sure that new guess is not an already guess word. If so, print out a warning
    # and get another guess from the user (easiest is to recursively call guess_word)
    #console.print(f"You've already guessed {guess}.", style="warning")

    # TODO: Check to make sure that the guess has the correct number of letters. If so, print out a warning
    # and get another guess from the user.

    # TODO: check to make sure that all letters are in ascii_letters. If not, print out a warning
    # and get another guess from the user

    return guess

def print_title(title):
    # Print the title
    print(title)
    # TODO: Add rich styling, here is an example
    #console.clear()
    #console.rule(f"[blue]:leafy_green: {title} :leafy_green:[/]\n")


if __name__ == "__main__":
    main()