count=input("e")
be = 0
while(int(count) >= 0):
    Bessietehcow = str(input("e"))
    Bessietehcow = list(Bessietehcow)
    Bessietehcow.reverse()
    Elsietehcow = Bessietehcow
    Elsietehcow.reverse()

    if (int(Bessietehcow[1]) >= 5):
        banswer = []
        Bessietehcow[0] = int(Bessietehcow[0]) + 1
        if (Bessietehcow[0] == 10):
            Bessietehcow[0] = 0
            Bessietehcow.insert(1)
    banswer.append(Bessietehcow[0])
    Bessietehcow = str(Bessietehcow)
    Bessietehcow = Bessietehcow.replace(" ", "")
    Bessietehcow = Bessietehcow.replace(",", "")
    Bessietehcow = Bessietehcow.replace("'", "")
    Bessietehcow = Bessietehcow.replace("[", "")
    Bessietehcow = Bessietehcow.replace("]", "")
    banswer.append(len(Bessietehcow))

    for i in int(len(Elsietehcow)):
        if (Elsietehcow[i-1] >= 5):
            Elsietehcow[i] += 1
        i+=1
    print(Elsietehcow)
    count = int(count) - 1
