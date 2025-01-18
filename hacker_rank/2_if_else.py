#https://www.hackerrank.com/challenges/py-if-else/

import math
import os
import random
import re
import sys

# Task
# Given an integer,n , perform the following conditional actions:
#
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 6, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
n = int(input("Give me a number."))

c = n % 2
if (c == 1):
    print("Weird")
elif (1 < n) and (n < 7):
    print("Not Weird")
elif (5 < n) and (n < 21):
    print("Weird")
elif (n > 20):
    print("Not Weird")