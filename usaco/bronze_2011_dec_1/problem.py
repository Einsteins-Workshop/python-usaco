# See https://usaco.org/index.php?page=viewproblem2&cpid=94

# Problem 1: Hay Bales [Brian Dean, 2011]
#
# The cows are at it again!  Farmer John has carefully arranged N (1 <= N <=
# 10,000) piles of hay bales, each of the same height.  When he isn't
# looking, however, the cows move some of the hay bales between piles, so
# their heights are no longer necessarily the same.  Given the new heights of
# all the piles, please help Farmer John determine the minimum number of hay
# bales he needs to move in order to restore all the piles to their original,
# equal heights.
#
# PROBLEM NAME: haybales
#
# INPUT FORMAT:
#
# * Line 1: The number of piles, N (1 <= N <= 10,000).
#
# * Lines 2..1+N: Each line contains the number of hay bales in a single
#         pile (an integer in the range 1...10,000).
#
# SAMPLE INPUT (file haybales.in):
#
# 4
# 2
# 10
# 7
# 1
#
# INPUT DETAILS:
#
# There are 4 piles, of heights 2, 10, 7, and 1.
#
# OUTPUT FORMAT:
#
#* Line 1: An integer giving the minimum number of hay bales that need
#        to be moved to restore the piles to having equal heights.
#
# SAMPLE OUTPUT (file haybales.out):
#
# 7

# Fill out the following function, which should return the correct answer for a file with
# the correct input file format.
def determine_solution(file_name):
    gimmiefiles = open(file_name, "r")
    next_line = gimmiefiles.readline()
    next_line = gimmiefiles.readline()
    sumofstacks = 0
    count = 0
    hayoutofplace = 0
    while next_line:
        sumofstacks = int(sumofstacks) + int(next_line)
        count = count + 1
        #print (count, sumofstacks, next_line)
        next_line=gimmiefiles.readline()
    average = sumofstacks / count
    gimmiefilesx2 = open(file_name, "r")
    next_line = gimmiefilesx2.readline()
    next_line = gimmiefilesx2.readline()
    #print(average, "p2")
    while next_line:
        hayoutofplace = hayoutofplace + abs(int(next_line) - average)
        next_line=gimmiefilesx2.readline()
        #print(hayoutofplace)
    #print(hayoutofplace/2)
    return int(hayoutofplace/2)

    next_line = gimmiefiles.readline()


# Proper format to be evaluated by USACO
# with open("ctiming.out", "w") as f:
#    f.write(str(determine_solution("ctiming.in")))
#    exit()

# Checking against all local files
for case in range(1, 11):
    input_file_name = f"data_files/I.{case}"
    with open(f"data_solutions/O.{case}", 'r') as input_file:
        correct_answer = input_file.readline().rstrip()
        print(f"For file {input_file_name} the correct answer is {correct_answer}")
        your_answer = str(determine_solution(input_file_name))
        if correct_answer != your_answer:
            print(f"Your answer of {your_answer} is not correct, try again.")
            exit()
