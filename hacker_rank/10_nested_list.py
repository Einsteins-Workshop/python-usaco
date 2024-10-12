#https://www.hackerrank.com/challenges/nested-list

# Given the names and grades for each student in a class of N students, store them in a nested list and print the
# name(s) of any student(s) having the second lowest grade.
#
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each
# name on a new line.
#
# Example
# records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]]
# The ordered list of scores is [20.0, 50,0], so the second lowest score is 50.0. There are two students with that
# score: ["beta", "alpha"]. Ordered alphabetically, the names are printed as:
#
# alpha
# beta

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())