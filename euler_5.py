# See https://projecteuler.net/problem=5

# 2520 is the smalles number that can be divided by each of the numbers from 1 to 10 without
# any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1
# to 20.

# Replace the below with your program.
print(2520)
selfDestruct=False
for x in range(20,100000000):
    for y in range(1, 21):
        selfDestruct=False
        if x%y!=0:
            selfDestruct=True
            break
    if selfDestruct:
        break
print(x)