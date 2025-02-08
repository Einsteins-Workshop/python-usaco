import random
def pickCard(alreadyPicked):
    numbers=["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
    suites=["Spades", "Hearts", "Diamonds", "Clubs"]
    attempt=" ".join([random.choice(numbers),"of",random.choice(suites)])
    while attempt in alreadyPicked:
        attempt = " ".join([random.choice(numbers), "of", random.choice(suites)])
    return attempt
def cardValue(card):
    cardsinorder = ['Ace of Spades', 'Ace of Hearts', 'Ace of Diamonds', 'Ace of Clubs', 'Two of Spades', 'Two of Hearts', 'Two of Diamonds', 'Two of Clubs', 'Three of Spades', 'Three of Hearts', 'Three of Diamonds', 'Three of Clubs', 'Four of Spades', 'Four of Hearts', 'Four of Diamonds', 'Four of Clubs', 'Five of Spades', 'Five of Hearts', 'Five of Diamonds', 'Five of Clubs', 'Six of Spades', 'Six of Hearts', 'Six of Diamonds', 'Six of Clubs', 'Seven of Spades', 'Seven of Hearts', 'Seven of Diamonds', 'Seven of Clubs', 'Eight of Spades', 'Eight of Hearts', 'Eight of Diamonds', 'Eight of Clubs', 'Nine of Spades', 'Nine of Hearts', 'Nine of Diamonds', 'Nine of Clubs', 'Ten of Spades', 'Ten of Hearts', 'Ten of Diamonds', 'Ten of Clubs', 'Jack of Spades', 'Jack of Hearts', 'Jack of Diamonds', 'Jack of Clubs', 'Queen of Spades', 'Queen of Hearts', 'Queen of Diamonds', 'Queen of Clubs', 'King of Spades', 'King of Hearts', 'King of Diamonds', 'King of Clubs']
    cardvaluesinorder = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    cardvalue=cardvaluesinorder[cardsinorder.index(card)]
    if cardvalue==1:
        while True:
            aceChoice=input(f"Would you like your {card} to be a 1 or 11?: ")
            if aceChoice=="11":
                cardvalue=11
                break
            elif aceChoice=="1":
                break
    return cardvalue
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
playercards=[]
playervalues=[]
playeramount=1
player=0
for i in range(playeramount):
    playercards.append([])
    playervalues.append(0)
shuffledDeck=shuffle()
for i in deal(2):
    print(f"You got a {i}!")
    playercards[player].append(i)
    playervalues[player]=cardValue(i)+playervalues[player]
print(f"Your total card value is {playervalues[player]}")
while True:
    hitbool=input("Do you want to hit? (Yes/No): ")
    if hitbool=="Yes":
        dealt=deal(1)[0]
        print(f"You got a {dealt}")
        playercards[player].append(dealt)
        playervalues[player]=cardValue(dealt)+playervalues[player]
        print(f"Your total card value is {playervalues[player]}")
        if playervalues[player]>21:
            print("You busted.")
            break
    elif hitbool=="No":
        break
    else:
        print("Please try again.")
