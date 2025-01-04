testCows=[]
for i in range(int(input("How many tests?: "))):
    testCows.append(int(input("Next cow please: ")))
for x in range(len(testCows)):
    y=0
    thing=len(str(testCows[x]))
    tataiedeada=testCows[x]/(10**thing)*10
    bessie=int(round(tataiedeada)*(10**thing)/10)
    print(bessie)
    tataiedeada=str(testCows[x]).replace(""," ").split()
    for bobbermeathen in range(thing):
        print(tataiedeada[thing-bobbermeathen-1])