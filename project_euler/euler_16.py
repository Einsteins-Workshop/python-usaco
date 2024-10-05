# https://projecteuler.net/problem=16

# 2^15 = 32768 and the sum of the digits is 3+2+7+6+8 = 26.
#
# What is the sum of the digits of the number 2^1000?
powerOf2=1
for i in range(1000):
    powerOf2=powerOf2*2
split=[]
powerOf2=str(powerOf2)
for x in range(len(powerOf2)):
    split.append(int(powerOf2[x]))
print(sum(split))