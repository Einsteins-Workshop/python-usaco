# See https://projecteuler.net/problem=3

# The prime factors of 13195 are 5, 7, 13, and 29.

# What is the largest prime factor of the number 600851475143

# Replace the below with your program.
import math
BeeegNumber=600851475143
BeeegNumber=int(BeeegNumber)
    
primer=[]
possiblePrimes=[]
for i in range(BeeegNumber):
    possiblePrimes.append(i+1)
possiblePrimes.remove(possiblePrimes[0])
for a in range(len(possiblePrimes)):
    if len(possiblePrimes)!=0:
        primer.append(possiblePrimes[0])
        for o in range(len(possiblePrimes)):
            if o>=len(possiblePrimes):
                break
            if possiblePrimes[o]%primer[-1]==0:
                possiblePrimes.remove(possiblePrimes[o])
    else:
        break
primeFactors=[]
beeegestPrimeFactor=0
print(primer)
while len(primer)>0:
    primethy=primer[0]
    primer.remove(primer[0])
    if BeeegNumber % primethy == 0:
        primeFactors.append(primethy)
        if primethy>beeegestPrimeFactor:
            beeegestPrimeFactor=primethy
print(beeegestPrimeFactor)