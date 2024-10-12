# See https://usaco.org/index.php?page=viewproblem2&cpid=95

# Problem 2: Cow Photography (Bronze) [Brian Dean, 2011]
#
# The cows are in a particularly mischievous mood today!  All Farmer John
# wants to do is take a photograph of the cows standing in a line, but they
# keep moving right before he has a chance to snap the picture.
#
# Specifically, FJ's N (1 <= N <= 20,000) cows are tagged with ID numbers
# 1...N.  FJ wants to take a picture of the cows standing in a line in a
# very specific ordering, represented by the contents of an array A[1...N],
# where A[j] gives the ID number of the jth cow in the ordering.  He arranges
# the cows in this order, but just before he can press the button on his
# camera to snap the picture, up to one cow moves to a new position in the
# lineup. More precisely, either no cows move, or one cow vacates her current
# position in the lineup and then re-inserts herself at a new position in the
# lineup.  Frustrated but not deterred, FJ again arranges his cows according
# to the ordering in A, but again, right before he can snap a picture, up to
# one cow (different from the first) moves to a new position in the lineup.
#
# The process above repeats for a total of five photographs before FJ gives
# up.  Given the contents of each photograph, see if you can reconstruct the
# original intended ordering A.  Each photograph shows an ordering of the
# cows in which up to one cow has moved to a new location, starting from the
# initial ordering in A.  Moreover, if a cow opts to move herself to a new
# location in one of the photographs, then she does not actively move in any
# of the other photographs (although she can end up at a different position
# due to other cows moving, of course).
#
# PROBLEM NAME: photo
#
# INPUT FORMAT:
#
# * Line 1: The number of cows, N (1 <= N <= 20,000).
#
# * Lines 2..5N+1: The next 5N lines describe five orderings, each one a
#         block of N contiguous lines.  Each line contains the ID of a
#         cow, an integer in the range 1..N.
#
# SAMPLE INPUT (file photo.in):
#
# 5
# 1
# 2
# 3
# 4
# 5
# 2
# 1
# 3
# 4
# 5
# 3
# 1
# 2
# 4
# 5
# 4
# 1
# 2
# 3
# 5
# 5
# 1
# 2
# 3
# 4
#
# INPUT DETAILS:
#
# There are 5 cows, with IDs 1, 2, 3, 4, and 5.  In each of the 5
# photos, a different cow moves to the front of the line (although the cows
# could have moved anywhere else, if they wanted).
#
# OUTPUT FORMAT:
#
# * Lines 1..N: The intended ordering A, one ID per line.
#
# SAMPLE OUTPUT (file photo.out):
#
# 1
# 2
# 3
# 4
# 5
#
# OUTPUT DETAILS:
#
# The correct original ordering A[1..5] is 1,2,3,4,5.


# Fill out the following function, which should return the correct answer for a file with
# the correct input file format.
def determine_solution(file_name):
    return "1\n2\n3\n4\n5\n"


# Proper format to be evaluated by USACO
# with open("photo.out", "w") as f:
#    f.write(str(determine_solution("photo.in")))
#    exit()

# Checking against all local files

for case in range(1, 11):
    input_file_name = f"data_files/I.{case}"
    with open(f"data_solutions/O.{case}", 'r') as input_file:
        lines = input_file.readlines()
        correct_answer = "".join(lines)
        print(f"For file {input_file_name} the correct answer is {','.join([x.rstrip() for x in lines])}")
        your_answer = str(determine_solution(input_file_name))
        if correct_answer != your_answer:
            print(f"Your answer of {your_answer} is not correct, try again.")
            exit()