import random
def shuffle():
    colors=["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
    picks=[]
    for i in range(len(colors)):
        picked=random.choice(colors)
        picks.append(picked)
        colors.remove(picked)
    return picks
shuffled=shuffle()
while True:
    dapotsinside=input("Guess your colors(Red, Orange, Yellow, Green, Blue, Purple): ")
    if str(dapotsinside)==str(shuffled):
        print("You won!!! Yay!")
    else:
        potsarecool=dapotsinside.split(", ")
        if len(potsarecool)==6 and "Red" in potsarecool and "Orange" in potsarecool and "Yellow" in potsarecool and "Green" in potsarecool and "Blue" in potsarecool and "Purple" in potsarecool:
            truedat=False
            print("No, but,")
            for i in range(len(shuffled)):
                if potsarecool[i] == shuffled[i]:
                    print(f"Number {i + 1} is correct.")
                    truedat=True
            if truedat==False:
                print("Everything is wrong")