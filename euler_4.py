# See https://projecteuler.net/problem=4

# A palindromic number reads the same both ways. The largest palindrome made from the product of
# two-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# Replace the below with your program.
def isbobbyapalendrome(x):
    x=str(x)
    y=x [::-1]
    y=int(y)
    x=int(x)
    if x==y:
        print("Yah, bobby is a palendrome")
        return True
    else:
        print("Nuh, bobby aint no palendrome")
        return False
z=0
for x in range(100, 1000):
    for y in range(100, 1000):
        if isbobbyapalendrome(x*y) and x*y>z:
            z=x*y
print(z)