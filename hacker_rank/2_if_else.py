#https://www.hackerrank.com/challenges/py-if-else/

import math
import os
import random
import re
import sys

# Task
# Given an integer, n, perform the following conditional actions:
#
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird


n = int(input("Please enter a number"))
if n % 2 == 1:
    print("Weird")
elif n>1 and n<6:
    print("Not Weird")
elif n>5 and n<21:
    print("Weird")
elif n>20 and n<100:
    print("Not Weird")
else:
    print("Please enter a number greater than 1 but less than 100.")