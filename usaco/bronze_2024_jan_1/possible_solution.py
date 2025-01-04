# See https://usaco.org/index.php?page=viewproblem2&cpid=1371

# Farmer John has an important task - figuring out what type of hay to buy for his cows.
#
# Farmer John's N cows (2≤N≤10^5) are numbered 1 through N and each cow likes exactly one type of hay h_i  (1≤hi_≤N).
# He wants all his cows to like the same type of hay.
#
# To make this happen, Farmer John can host focus groups. A focus group consists of getting all cows in a contiguous
# range numbered i to j , inclusive, together for a meeting. If there is a type of hay that more than half the cows in
# the group like, then after the focus group finishes meeting, all cows end up liking that type of hay. If no such type
# of hay exists, then no cows change the type of hay they like. For example, in focus group consisting of a range of 16
# cows, 9 or more of them would need to have the same hay preference to cause the remaining cows to switch their
# preference to match.
#
# Farmer John wants to know which types of hay can become liked by all cows simultaneously. He can only host one focus
# group at a time, but he can run as many focus groups as necessary to get all cows to like the same type of hay.
#
# INPUT FORMAT (input arrives from the terminal / stdin):
# The first will consist of an integer T, denoting the number of independent test cases (1≤T≤10).
#
# The first line of each test case consists of N.
#
# The second line consists of N integers, the favorite types of hay h_i for the cows in order.
#
# It is guaranteed that the sum of N  over all test cases does not exceed 200000.
#
# OUTPUT FORMAT (print output to the terminal / stdout):
# Output T lines, one line per test case.
# If it is possible to make all cows like the same type of hay simultaneously, output all possible such types of hay in
# increasing order. Otherwise, output −1. When printing a list of numbers on the same line, separate adjacent numbers
# with a space, and be sure the line does not end with any extraneous spaces.
#
# SAMPLE INPUT:
# 5
# 5
# 1 2 2 2 3
# 6
# 1 2 3 1 2 3
# 6
# 1 1 1 2 2 2
# 3
# 3 2 3
# 2
# 2 1
# SAMPLE OUTPUT:
# 2
# -1
# 1 2
# 3
# -1
# In the sample input, there are 5 test cases.
#
# In the first test case, it is only possible to make all cows like type 2. FJ can do this by running a single focus
# group with all cows.
#
# In the second test case, we can show that no cows will change which type of hay they like.
#
# In the third test case, it is possible to make all cows like type 1 by running three focus groups - first by having
# cows 1 through 4 in a focus group, then by having cows 1 through 5 in a focus group, then by having cows 1 through 6
# in a focus group. By similar logic, using cows 3 through 6, cows 2 through 6, then cows 1 through 6, we can make all
# cows like type 2.
#
# In the fourth test case, it is possible to make all cows like type 3 by running a single focus group with all cows.
#
# In the fifth test case, we can show that no cows will change which type of hay they like.

# Fill out the following function, which should return the correct answer for a file with
# the correct input file format.
def determine_solution(file_handle):
    case_count = int(file_handle.readline().rstrip())

    cases = []
    for _ in range(case_count):
        file_handle.readline()
        opinion_line = file_handle.readline().rstrip()
        cases.append([int(x) for x in opinion_line.split(" ")])

    return "\n".join([poll_opinions(x) for x in cases]) + "\n"

def poll_opinions(starting_state):
    if len(starting_state) == 1:
        return str(starting_state[0])
    if len(starting_state) == 2:
        if starting_state[0] == starting_state[1]:
            return str(starting_state[0])
        else:
            return str(-1)
    possible_winning_hay = set()
    for i in range(len(starting_state) - 2):
        if (starting_state[i] == starting_state[i+1]) or (starting_state[i] == starting_state[i+2]):
            possible_winning_hay.add(starting_state[i])
    if starting_state[-1] == starting_state[-2]:
        possible_winning_hay.add(starting_state[-1])
    if len(possible_winning_hay) == 0:
        return str(-1)
    return " ".join([str(x) for x in sorted(possible_winning_hay)])


# Proper format to be evaluated by USACO
#  print(str(determine_solution(sys.stdin)))
#  exit()

# Checking against all local files
for case in range(1, 15):
    input_file_name = f"data_files/{case}.in"
    with open(f"data_solutions/{case}.out", 'r') as input_file:
        correct_answer = ''.join(input_file.readlines())
        formatted_correct_answer = correct_answer.replace("\n", ' ')
        #print(f"For file {input_file_name} the correct answer is {formatted_correct_answer}")
        print(f"Working on {input_file_name}")
        your_answer = determine_solution(open(input_file_name, 'r'))
        if correct_answer != your_answer:
            formatted_your_answer = your_answer.replace("\n", " ")
            #print(f"Your answer of {formatted_your_answer} is not correct, try again.")
            import difflib
            diff = difflib.unified_diff(correct_answer, your_answer)
            for line in diff:
                print(line)
            #print(your_answer)
            exit()
