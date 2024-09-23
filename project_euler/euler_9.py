# See https://projecteuler.net/problem=9

# A Pythagorean triplet is a set of three natural numbers, z < b < c, for which
#    a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.

# Find the product abc.

# Replace the below with your program.
for n in range(1000):
    for m in range(1000):
        a=n*n-m*m
        b=2*m*n
        c=n*n+m*m
        if a+b+c==1000 and a*b*c>1:
            print(a*b*c)
            break