# https://projecteuler.net/problem=20
#
# n! means n x (n-1) x ... x 3 x 2 x 1
# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 3628800,
# and the sum of the digits in the number 10! is 3+6+2+8+8+0+0=27
#
# Find the sum of the digits in the number 100!


# Replace the below with your program.
fact=1
facts=[]
for x in range(1, 100+1):
    fac=fac*x
fac=str(fac)
for i in range(len(fac)):
    facts.append(int(fac[i]))
print(sum(facts))