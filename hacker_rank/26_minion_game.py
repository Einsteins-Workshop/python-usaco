# https://www.hackerrank.com/challenges/the-minion-game
#
# Kevin and Stuart want to play the 'The Minion Game'.
# Both players are given the same string,S .
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
# A player gets +1 point for each occurrence of the substring in the string S.
#
# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
#
# For example, in BANANA, Stuart will core 12 points and Kevin will have 10 points.
# Your task is to determine the winner of the game and their score.
#
# Input Format
#
# A single line of input containing the string S.
#
# Output Format
# The winner's name and score, separated by a space on one line, or Draw if there is no winner
#
# Sample Input
# BANANA
#
# Sample Output
# Stuart 12
#
def minion_game(string):
    # your code goes here
    print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)