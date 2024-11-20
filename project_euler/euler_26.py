# https://projecteuler.net/problem=26
#
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with
# denominators 2 to 10 are given:
#
# 1/2 = 0.5
# 1/3 = 0.(3)
# 1/4 = 0.25
# 1/5 = 0.2
# 1/6 = 0.1(6)
# 1/7 = 0.(142857)
# 1/8 = 0.125
# 1/9 = 0.(1)
# 1/10 = 0.1
#
# Where 0.1(6) means 0.166666...., and has a 1-digit recurring cycle. It can be seen that
# 1/7 has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal
# fraction part.

# Replace the below with your program.
n=0
counter=1
ab=0
primer=[2]
for i in range(200000):
    if i>2:
        someSortOfVarible=i**0.5
        for x in primer:
            if i%x==0:
                break
            elif x>someSortOfVarible:
                primer.append(i)
                break
for a in range(-1000,1000):
    for b in range(-1000,1000):
        while n**2+a*n+b in primer:
            n=n+1
        if n>counter:
            counter=n
            ab=a*b
            print(ab)
