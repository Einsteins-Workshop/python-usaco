import random
def pickCard(alreadyPicked):
    numbers=["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
    suites=["Spades", "Hearts", "Diamonds", "Clubs"]
    attempt=" ".join([random.choice(numbers),"of",random.choice(suites)])
    while attempt in alreadyPicked:
        attempt = " ".join([random.choice(numbers), "of", random.choice(suites)])
    return attempt
def shuffle():
    picks=[]
    for i in range(52):
        picks.append(pickCard(picks))
    return picks
def deal(amount):
    deals=[]
    for i in shuffledDeck:
        amount=amount-1
        deals.append(i)
        shuffledDeck.remove(i)
        if amount==0:
            return deals

shuffledDeck=shuffle()
for i in deal(2):
    print(f"You got a {i}!")
    if player==1:
        player1cards.append[i]
while True:
    hitbool=input("Do you want to hit? (Yes/No): ")
    if hitbool=="Yes":
        print(f"You got a {deal(1)[0]}")
    elif hitbool=="No":
        break
    else:
        print("Please try again.")
