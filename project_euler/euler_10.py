# See https://projecteuler.net/problem=10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# Replace the below with your program.
testing = 0
sum = 5
primefound = [2, 3]
primetesting = 4
while(primetesting<2000001):
    for prime in primefound:
        if (primetesting % prime == 0):
            testing = "change"
            break
    if (str(testing) == "change"):
        primetesting=primetesting+1
    else:
        primefound.append(primetesting)
        sum=sum+primetesting
        primetesting = primetesting + 1
    testing=0
print (primefound)
print (sum)