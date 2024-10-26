# https://www.hackerrank.com/challenges/merge-the-tools
#
# Consider the following:
# * A string s of length n where s = c_0 c_1 ... c_(n-1)
# * An integer k where k is a factor of n
#
# We can split s into n/k substrings where each substring t_i consists of a
# contiguous block of k characters in s. Then use each t_i to create string u_i such that:
# * The characters in u_i are a subsequence of the characters in t_i
# * Any repeat occurrence of a character is removed from the string such that each
#   character in u_i occurs exactly once. In other words, if the character at some index
#   j in t_i occurs at a previous index < j in t_i, then do not include the character in
#   string u_i
# Given s and k, print n/k lines where each line i denotes string u_i
#
# Example:
# s = "AAABCADDE"
# k = 3
#
# There are three substrings of length 3 to consider: "AAA". "BCA", "DDE". The first
# substring is all 'A' characters so u_1 = 'A'. The second substring has all distinct
# characters, so u_2 in 'BCA'. The third character has dwo different characters so
# u_3 = 'DE'. Note that a subsequence maintains the original order of characters in each
# subsequence. The order of characters in each subsequence shown is important.
#
# Input Format
# The first line contains a single string, s.
# The second line contains an integer, k, the length of each substring.
#
# Output Format
# Print each subsequence on a new line. There will be n/k  of them. No return value is expected.
#
# Sample Input
# STDIN       Function
# -----       --------
# AABCAAADA   s = 'AABCAAADA'
# 3           k = 3
#
# Sample Output
# AB
# CA
# AD
def merge_the_tools(string, k):
    # your code goes here
    print()
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)