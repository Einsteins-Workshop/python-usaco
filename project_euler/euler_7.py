# See https://projecteuler.net/problem=7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the
# 6th prime is 13.

# What is the 10001st prime number?

# Replace the below with your program.
primer=[]
possiblePrimes=[]
for i in range(200000):
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
print(primer[10000])