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
# If n is even and in the inclusive range of 6 to 2p, print Weird
# If n is even and greater than 20, print Not Weird

if __name__ == '__main__':
    n = int(input().strip())