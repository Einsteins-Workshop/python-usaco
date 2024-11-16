# https://projecteuler.net/problem=25
# The Fibonacci sequence is defined by the recurrence relation:
# F_n = F_{n-1} + F_{n-2}, where F_1 = 1 and F_2 = 1
#
# Hence the first 12 terms will be:
# F_1 = 1, F_2=1, F_3=2, F_4=3, F_5=5, F_6=8, F_7=13, F_8=21, F_9=34, F_10=55, F_11=89, F_12=144
#
# The twelvth term is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci squence to contain 1000 digits?

# Replace the below with your program.
fibi=[]
def fib(x):
    n1=1
    n2=1
    for i in range(x):
        fibi.append(n1)
        n3=n1+n2
        n1=n2
        n2=n3
found=False
x=0
fib(9999)
while not found:
    x=x+1
    if len(str(fibi[x]))==1000:
        print(x+1)
        found=True