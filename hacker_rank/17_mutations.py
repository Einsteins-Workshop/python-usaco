# https://www.hackerrank.com/challenges/python-mutations
# We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
#
# Let's try to understand this with an example.
#
# You are given an immutable string, and you want to make changes to it.
#
# >>> string = "abracadabra"
#
# You are given an immutable string, and you want to make changes to it.
#
# >>> print string[5]
# a
#
# What if you would like to assign a value?
# >>> string[5] = 'k'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment
#
# How would you approach this?
# One solution is to convert the string to a list and then change the value.
# >>> string = "abracadabra"
# >>> l = list(string)
# >>> l[5] = 'k'
# >>> string = ''.join(l)
# >>> print string
# abrackdabra
#
# Another approach is to slice the string and join it back.
# >>> string = string[:5] + "k" + string[6:]
# >>> print string
# abrackdabra

def mutate_string(string, position, character):
    return

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)