# https://www.hackerrank.com/challenges/text-wrap
# You are given a string s and width w.
# Your task is to wrap the string into a paragraph of width w.
#
# Input Format
# The first line contains a string, string.
# The second line contains the width, max_width.
#
# Returns
# A single string with newline characters ('\n') where the breaks should be
#
# Sample Input
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
#
# Sample Output
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

import textwrap

def wrap(string, max_width):
    return

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)