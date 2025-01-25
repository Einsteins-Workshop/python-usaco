    # https://projecteuler.net/problem=25
# The Fibonacci sequence is defined by the recurrence relation:
# F_n = F_{n-1} + F_{n-2}, where F_1 = 1 and F_2 = 1
#
# Hence the first 12 terms will be:
# F_1 = 1, F_2=1, F_3=2, F_4=3, F_5=5, F_6=8, F_7=13, F_8=21, F_9=34, F_10=55, F_11=89, F_12=144
#
# The twelvthh term is the first term to contain three digits.

# What is the index of the first term in the Fibonacci squence to contain 1000 digits?
import sys
totallength=input("howbigdigitsdouwant")
if (int(totallength) > 700): {
    sys.set_int_max_str_digits(int(totallength)+1)
}
fiblist = [1, 1]
count = 2
addthemalltogether = 2
ready = "no"
def fib_next(fibl):
    count+1
    return fibl[1],fibl[0]+fibl[1]

while (len(str(fiblist[1])) < int(totallength)):
    fiblist = fib_next(fiblist)
    addthemalltogether = addthemalltogether + fiblist[1]
    print(len(str(fiblist[1])) / int(totallength) * 100,"%")

print(count, len(str(fiblist[1])), fiblist[1])
while (ready != "forsure"):
    ready=input("are you ready")
print(addthemalltogether)
