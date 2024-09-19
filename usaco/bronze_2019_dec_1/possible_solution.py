# See https://usaco.org/index.php?page=viewproblem2&cpid=963

# In order to improve their physical fitness, the cows have taken up gymnastics! Farmer John
# designates his favorite cow Bessie to coach the N other cows and to assess their progress
# as they learn various gymnastic skills.

# In each of K practice sessions (1 ≤ K ≤10) Bessie ranks the N cows according to their
# performance (1 ≤ N ≤ 20). Afterward, she is curious about the consistency in these rankings.
# A pair of two distinct cows is consistent if one cow did better than the other one in every
# practice session.

# Help Bessie compute the total number of consistent pairs.

# INPUT FORMAT (file gymnastics.in):

# The first line of the input file contains two positive integers K and N. The next K
# lines will each contain the integers 1…N in some order, indicating the rankings of
# the cows (cows are identified by the numbers 1…N). If A appears before B in one of
# these lines, that means cow A did better than cow B.
#

# OUTPUT FORMAT (file gymnastics.out):

# Output, on a single line, the number of consistent pairs.

# SAMPLE INPUT:
# 3 4
# 4 1 2 3
# 4 1 3 2
# 4 2 1 3

# SAMPLE OUTPUT:
# 4
# The consistent pairs of cows are (1,4), (2,4), (3,4), and (1,3).

def import_data(file_name):
    with open(file_name, 'r') as file:
        first_line = file.readline().rstrip().split(' ')
        contest_count = int(first_line[0])
        cow_count = int(first_line[1])

        contest_result_list = []
        for contest in range(1, contest_count + 1):
            string_results = file.readline().rstrip().split(' ')
            contest = {}
            for idx, x in enumerate(map(lambda y: int(y), string_results)):
                contest[x] = idx
            contest_result_list.append(contest)
        return contest_count, cow_count, contest_result_list


def contest_winner(cow_1, cow_2, contest):
    return cow_1 if contest[cow_1] < contest[cow_2] else cow_2


def is_dominant_pair(cow_1, cow_2, results, contest_count):
    first_contest_winner = contest_winner(cow_1, cow_2, results[0])
    contest_winners = map(lambda x: contest_winner(cow_1, cow_2, results[x]) == first_contest_winner,
                          range(1, contest_count)
                          )
    return all(contest_winners)


def determine_solution(file_name):
    contests, cows, contest_results = import_data(file_name)

    dominant_pair_count = 0
    for i in range(1, cows + 1):
        for j in range(i + 1, cows + 1):
            if is_dominant_pair(i, j, contest_results, contests):
                dominant_pair_count += 1
    return dominant_pair_count


# Proper format to be evaluated by USACO
# with open("gymnastics.out", "w") as f:
#    f.write(str(determine_solution("gymnastics.in")))
#    exit()

# Checking against all local files
for case in range(1, 11):
    input_file_name = f"data_files/{case}.in"
    with open(f"data_solutions/{case}.out", 'r') as input_file:
        correct_answer = input_file.readline().rstrip()
        print(f"For file {input_file_name} the correct answer is {correct_answer}")
        your_answer = str(determine_solution(input_file_name))
        if correct_answer != your_answer:
            print(f"Your answer of {your_answer} is not correct, try again.")
            exit()