# See https://projecteuler.net/problem=5

# 2520 is the smalles number that can be divided by each of the numbers from 1 to 10 without
# any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1
# to 20.

# Replace the below with your program.
while True:
    for y in range(1, 21):
        if x%y!=0:
            failed=True
            break
    if failed==True:
        x=x+1
    else:
        break
print(x)