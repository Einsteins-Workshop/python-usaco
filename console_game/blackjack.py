import random
def pickCard(alreadyPicked):
    numbers=["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
    suites=["Spades", "Hearts", "Diamonds", "Clubs"]
    attempt=" ".join([random.choice(numbers),"of",random.choice(suites)])
    while attempt in alreadyPicked:
        attempt = " ".join([random.choice(numbers), "of", random.choice(suites)])
    return attempt
def cardValue(card, player):
    cardsinorder = ['Ace of Spades', 'Ace of Hearts', 'Ace of Diamonds', 'Ace of Clubs', 'Two of Spades', 'Two of Hearts', 'Two of Diamonds', 'Two of Clubs', 'Three of Spades', 'Three of Hearts', 'Three of Diamonds', 'Three of Clubs', 'Four of Spades', 'Four of Hearts', 'Four of Diamonds', 'Four of Clubs', 'Five of Spades', 'Five of Hearts', 'Five of Diamonds', 'Five of Clubs', 'Six of Spades', 'Six of Hearts', 'Six of Diamonds', 'Six of Clubs', 'Seven of Spades', 'Seven of Hearts', 'Seven of Diamonds', 'Seven of Clubs', 'Eight of Spades', 'Eight of Hearts', 'Eight of Diamonds', 'Eight of Clubs', 'Nine of Spades', 'Nine of Hearts', 'Nine of Diamonds', 'Nine of Clubs', 'Ten of Spades', 'Ten of Hearts', 'Ten of Diamonds', 'Ten of Clubs', 'Jack of Spades', 'Jack of Hearts', 'Jack of Diamonds', 'Jack of Clubs', 'Queen of Spades', 'Queen of Hearts', 'Queen of Diamonds', 'Queen of Clubs', 'King of Spades', 'King of Hearts', 'King of Diamonds', 'King of Clubs']
    cardvaluesinorder = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    cardvalue=cardvaluesinorder[cardsinorder.index(card)]
    if cardvalue==1:
        while True:
            if player=="Player":
                aceChoice=input(f"Would you like your {card} to be a 1 or 11?: ")
            else:
                aceChoice="1"
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
score=0
games=0
while True:
    games=games+1
    playercards=[]
    playervalues=[]
    playercards.append([])
    playervalues.append(0)
    shuffledDeck=shuffle()
    for i in deal(2):
        print(f"You got a {i}!")
        playercards[0].append(i)
        playervalues[0]=cardValue(i, "Player")+playervalues[0]
    print(f"Your total card value is {playervalues[0]}")
    while True:
        hitbool=input("Hit or Stand?: ")
        if hitbool=="Hit":
            print(f"You {hitbool}")
            dealt=deal(1)[0]
            print(f"You got a {dealt}")
            playercards[0].append(dealt)
            playervalues[0]=cardValue(dealt, "Player")+playervalues[0]
            print(f"Your total card value is {playervalues[0]}")
            if playervalues[0]>21:
                print("You busted.")
                break
        elif hitbool=="Stand":
            print(f"You {hitbool}")
            break
        else:
            print("Please try again.")
    computercards=[]
    computervalues=[]
    computervalues.append(0)
    for i in deal(2):
        print(f"I got a {i}.")
        computercards.append(i)
        computervalues[0]=cardValue(i, "Computer")+computervalues[0]
    print(f"My total card value is {computervalues[0]}")
    while True:
        if sum(computervalues)<sum(playervalues) and 21>=playervalues[0]:
            print("I hit")
            dealt=deal(1)[0]
            print(f"I got a {dealt}")
            computercards.append(dealt)
            computervalues[0]=cardValue(dealt,"Computer")+computervalues[0]
            print(f"My total card value is {computervalues[0]}")
            if computervalues[0]>21:
                print("I busted.")
                break
        else:
            print("I stand")
            break
    tmpscore=score
    if sum(playervalues)>21:
        print("I won. Better luck next time.")
        score=score-sum(computervalues)
    elif sum(computervalues)>21:
        print("You won!!! You beat me. Good job.")
        score=score+sum(playervalues)
    else:
        if sum(playervalues)>sum(computervalues):
            print("You won!!! You beat me. Good job.")
            score=score+sum(playervalues)
        elif sum(computervalues)>sum(playervalues):
            print("I won. Better luck next time.")
            score=score-sum(computervalues)
        else:
            if len(playercards[0])>len(computercards):
                print("You won!!! You beat me. Good job.")
                score=score+sum(playervalues)
            elif len(computercards)>len(playercards[0]):
                print("I won. Better luck next time.")
                score=score-sum(computervalues)
            else:
                print("We tied. I hope you're happy.")
                score=score+sum(playervalues)-sum(computervalues)
    if input("Play another round?: ")=="No":
        break
    else:
        if score-tmpscore<0:
            scorechange="lost"
        else:
            scorechange="gained"
        print(f"Your score is {score}. You {scorechange} {score-tmpscore} score last round.")
print(f"You final score was {score}")
if score< 0:
    scorechange="lost"
else:
    scorechange="gained"
print(f"On average, you {scorechange} {score/games} score per game.")