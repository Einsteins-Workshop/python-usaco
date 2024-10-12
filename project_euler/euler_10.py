# See https://projecteuler.net/problem=10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# Replace the below with your program.
primer=[2]
for i in range(2000000):
    gogo=True
    if i>2:
        for x in primer:
            if i%x==0:
                gogo=False
            print(f"{(round((i / 2000000) * 100)) / 100}% done, {gogo}, {primer}")
        if gogo:
            primer.append(i)
print(sum(primer))