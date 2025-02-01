import random
choice1=str("R")
choice2=str("O")
choice3=str("Y")
choice4=str("G")
choice5=str("B")
choice6=str("P")

# How to play this game:
# Hit start, or run the command
# python mastermind.py
# in console.

# How to use different options:
# Change the variables.
# Example:
# choice1=str("R") --> choice1=str(1)

# How to add a new option:
# Ctrl+F to find all instances of "choice6"
# Following the syntax of the stuff around "choice6", add "choice7" behind it.
# Add a new variable named "choice7" and set it to str(Whatever you want here)
def shuffle():
    choices=[choice1, choice2, choice3, choice4, choice5, choice6]
    picks=[]
    for i in range(len(choices)):
        picked=random.choice(choices)
        picks.append(picked)
        choices.remove(picked)
    return picks
score=0
while True:
    shuffled=shuffle()
    while True:
        userGuess=input(f"Pick your choices out of {choice1}, {choice2}, {choice3}, {choice4}, {choice5}, {choice6}. \nMake sure to use this exact syntax: {choice1}, {choice2}, {choice3}, {choice4}, {choice5}, {choice6} \nNow, what is your guess?: ").split(", ")
        if userGuess==shuffled:
            break
        else:
            if len(userGuess)==6 and choice1 in userGuess and choice2 in userGuess and choice3 in userGuess and choice4 in userGuess and choice5 in userGuess and choice6 in userGuess:
                truedat=False
                print("No, but,")
                score=score-1
                for i in range(len(shuffled)):
                    if userGuess[i] == shuffled[i]:
                        print(f"Number {i + 1} is correct.")
                        truedat=True
                if truedat==False:
                    print("Everything is wrong")
    print("You won!!! Yay!")
    score=score+10
    print(f"Your score is {score}.")
    if input("Would you like to play again?(Yes/No): ")=="No":
        break
print(f"Goodbye. Your final score was: {score}.")