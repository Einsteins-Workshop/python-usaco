# See https://projecteuler.net/problem=6

# The sum of squares of the first ten natural numbers is:
#    1^2+2^2+...+10^2=385.

# The square of the sum of the first ten natural numbers is:
# (1+2+...+10)^2 = 55^2 = 3025.

# Hence the difference between the sum of the squares of the first ten natural numbers and the
# square of the sum is 3025-385 = 2650

# Find the difference between the sum of the squares of the first one hundred natural numbers
# and the square of the sum.

# Replace the below with your program.
sqofsu=0
suofsq=0
for x in range(1,101):
    sqofsu=sqofsu+x
    suofsq=suofsq+x*x
sqofsu=sqofsu*sqofsu
print(sqofsu-suofsq)