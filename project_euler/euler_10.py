# See https://projecteuler.net/problem=10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# Replace the below with your program.
primer=[]
possiblePrimes=[]
for i in range(2000000):
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
print(sum(primer))