# https://projecteuler.net/problem=34
#
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: As 1! = 1 and 2! = 2 are not sums, they are not included.
def factorialificate(numberatoration):
    letsnameavariblebob=1
    for iliedandnameditsally in range(numberatoration):
        letsnameavariblebob=letsnameavariblebob*(iliedandnameditsally+1)
    return letsnameavariblebob
def isFactorial(sally):
    sally=str(sally)
    lolihaveabobtoo=0
    for taco in sally:
        lolihaveabobtoo=lolihaveabobtoo+factorialificate(int(taco))
    return str(lolihaveabobtoo)==sally
x=1
tacocat=0
for x in range(9999999):
    if isFactorial(x) and x>2:
        tacocat=tacocat+x
print(tacocat)