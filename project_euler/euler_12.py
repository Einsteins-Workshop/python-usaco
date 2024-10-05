# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 28.

# The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55

# Let us list the factors of the first seven triangle numbers:

# 1: 1
# 3: 1, 3
# 6: 1, 2, 3, 6

# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?

# Replace the below with your program.
x=0
tri=0
while True:
    x=x+1
    tri=x+tri
    triFactors=[]
    for i in range(1,len(str(tri))+1):
        if tri%i==0:
            triFactors.append(i)
    if len(triFactors)>=500:
        print(tri)
        break