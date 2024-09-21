# See https://projecteuler.net/problem=1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9.
# The sum of these multiples is 23.

# Find the sum of all multiples of 3 or 5 below 1000

# Replace the below with your program.
Sum = 0
threecount = 0
fivecount = 0
def testcurrent(Test):
    if ((Test/3).is_integer()):
        return (3)
    elif ((Test/5).is_integer()):
        return (5)
    else:
        return False

for Current in range(1000):
    if (testcurrent(Current) == 3):
        threecount += 1
        Sum = Sum + Current
        print (Current)
    elif (testcurrent(Current) == 5):
        fivecount += 1
        Sum = Sum + Current
        print (Current)
    else:
        Current += 1
print (Sum, threecount, fivecount)