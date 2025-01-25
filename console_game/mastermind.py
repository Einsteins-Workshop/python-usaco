import random
def shuffle():
    colors=["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
    picks=[]
    for i in range(len(colors)):
        picked=random.choice(colors)
        picks.append(picked)
        colors.remove(picked)
    return picks
score=0
while True:
    shuffled=shuffle()
    while True:
        dapotsinside=input("Guess your colors(Red, Orange, Yellow, Green, Blue, Purple). \nMake sure to use this syntax: Red, Orange, Yellow, Green, Blue, Purple: ")
        if dapotsinside.split(", ")==shuffled:
            break
        else:
            potsarecool=dapotsinside.split(", ")
            if len(potsarecool)==6 and "Red" in potsarecool and "Orange" in potsarecool and "Yellow" in potsarecool and "Green" in potsarecool and "Blue" in potsarecool and "Purple" in potsarecool:
                truedat=False
                print("No, but,")
                score=score-1
                for i in range(len(shuffled)):
                    if potsarecool[i] == shuffled[i]:
                        print(f"Number {i + 1} is correct.")
                        truedat=True
                if truedat==False:
                    print("Everything is wrong")
    print("You won!!! Yay!")
    score=score+10
    if input("Play again?(Yes/No): ")=="No":
        break
print(f"Goodbye. Your final score was: {score}.")