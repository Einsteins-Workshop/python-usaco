# See https://usaco.org/index.php?page=viewproblem2&cpid=85

# Bessie the cow is just learning how to convert numbers between different
# bases, but she keeps making errors since she cannot easily hold a pen
# between her two front hooves.
#
# Whenever Bessie converts a number to a new base and writes down the result,
# she always writes one of the digits wrong.  For example, if she converts
# the number 14 into binary (i.e., base 2), the correct result should be
# "1110", but she might instead write down "0110" or "1111".  Bessie never
# accidentally adds or deletes digits, so she might write down a number with
# a leading digit of "0" if this is the digit she gets wrong.
#
# Given Bessie's output when converting a number N into base 2 and base 3,
# please determine the correct original value of N (in base 10). You can
# assume N is at most 1 billion, and that there is a unique solution for N.
#
# Please feel welcome to consult any on-line reference you wish regarding
# base-2 and base-3 numbers, if these concepts are new to you.
# INPUT FORMAT:
#
# * Line 1: The base-2 representation of N, with one digit written
#         incorrectly.
#
# * Line 2: The base-3 representation of N, with one digit written
#         incorrectly.
#
# SAMPLE INPUT (file digits.in):
#
# 1010
# 212
#
# INPUT DETAILS:
#
# When Bessie incorrectly converts N into base 2, she writes down
# "1010".  When she incorrectly converts N into base 3, she writes down "212".
#
# OUTPUT FORMAT:
#
# * Line 1: The correct value of N.
#
# SAMPLE OUTPUT (file digits.out):
#
# 14
#
# OUTPUT DETAILS:
#
# The correct value of N is 14 ("1110" in base 2, "112" in base 3).

# Fill out the following function, which should return the correct answer for a file with
# the correct input file format.
def determine_solution(file_name):
    return 14


# Proper format to be evaluated by USACO
# with open("digits.out", "w") as f:
#    f.write(str(determine_solution("digits.in")))
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
