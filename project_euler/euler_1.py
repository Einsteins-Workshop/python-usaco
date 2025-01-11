# See https://projecteuler.net/problem=1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9.
# The sum of these multiples is 23.

# Find the sum of all multiples of 3 or 5 below 1000

# Replace the below with your program
total = 0
for x in range(1000):
    c = x % 3
    d = x % 5
    if (c == 0):
        total = total + x
    elif (d == 0):
        total = total + x
print(total)


#Yay! I got it correct! 1/4/2025
#n =
#numbers = (5*n)
#print(numbers)