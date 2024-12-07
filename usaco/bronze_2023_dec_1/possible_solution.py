# See https://usaco.org/index.php?page=viewproblem2&cpid=1347

# Farmer John's cows have quite the sweet tooth, and they especially enjoy eating candy canes! FJ has N
#  total cows, each with a certain initial height and he wants to feed them M
#  candy canes, each also of varying height (1≤N,M≤2⋅105).
#
# FJ plans to feed the candy canes one by one to the cows, in the order they are given in the input.
# To feed a candy cane to his cows, he will hang the candy cane so that initially the candy cane is just
# touching the ground. The cows will then line up one by one, in the order given by the input, and go up
# to the candy cane, each eating up to their height (since they cannot reach any higher). The candy cane
# stays suspended in place where it is initially set up and is not lowered to the ground, even after cows
# eat the bottom of the candy cane. It is possible a cow may eat nothing during her turn, if the base of
# the candy cane is already above that cow's height. After every cow has had their turn, the cows grow in
# height by how many units of candy cane they ate, and Farmer John hangs the next candy cane and the cows
# repeat the process again (with cow 1 again being the first to start eating the next candy cane).
#
# INPUT FORMAT (input arrives from the terminal / stdin):
# The first line contains N and M.
# The next line contains the initial heights of the N cows, each in the range [1,10^9].
#
# The next line contains the heights of the M candy canes, each in the range [1,10^9].
#
# OUTPUT FORMAT (print output to the terminal / stdout):
# The final heights of each of the N cows on separate lines.
#
# SAMPLE INPUT:
# 3 2
# 3 2 5
# 6 1
# SAMPLE OUTPUT:
# 7
# 2
# 7
# The first candy cane is 6 units tall.
#
# The first cow eats the portion of the first candy cane up to height 3, after which the remaining portion of
# the first candy cane occupies heights [3,6].
# The second cow is not tall enough to eat any of the remaining portion of the first candy cane.
# The third cow eats two additional units of the first candy cane. The remaining portion of the first candy cane,
# occupying heights [5,6], is not eaten.
# Next, each cow grows by the amount she ate, so the heights of the cows become [3+3,2+0,5+2]=[6,2,7] .
#
# The second candy cane is 1 unit tall, and the first cow eats all of it.
#
# SCORING:
# Inputs 2-10: N,M≤10^3
# Inputs 11-14: No additional constraints.
# Problem credits: Agastya Goel

# Fill out the following function, which should return the correct answer for a file with
# the correct input file format.
def determine_solution(file_name):
    cows = []
    cow_candidates = []
    last_cow_height = 0
    canes = []
    with open(file_name, 'r') as file:
        file.readline()
        for cow_string in file.readline().rstrip().split(' '):
            cow_height = int(cow_string)
            new_cow = Cow(cow_height)
            if cow_height > last_cow_height:
                cow_candidates.append(new_cow)
                last_cow_height = cow_height
            cows.append(new_cow)

        canes = [int(cane_string) for cane_string in file.readline().rstrip().split(' ')]

    for cane in canes:
        current_eaten = 0
        counter = 0
        while counter < len(cow_candidates):
            cow = cow_candidates[counter]
            if cow.height() >= cane:
                # Cow eats the rest of the cane
                cow.eat(cane - current_eaten)
                break
            elif cow.height() > current_eaten:
                # Cow eats up to height
                new_current_eaten = cow.height()
                cow.eat(new_current_eaten - current_eaten)
                current_eaten = new_current_eaten
                counter += 1
            else:
                # Sad cow is shorter than her prior, so cannot eat any longer
                del cow_candidates[counter]

    return "".join([f"{cow.height()}\n" for cow in cows])


class Cow:
    def __init__(self, height):
        self.__height = height

    def __repr__(self):
        return str(self.__height)

    def height(self):
        return self.__height

    def eat(self, length):
        self.__height += length


# Proper format to be evaluated by USACO
# with open("gymnastics.out", "w") as f:
#    f.write(str(determine_solution("gymnastics.in")))
#    exit()

# Checking against all local files
for case in range(1, 15):
    input_file_name = f"data_files/{case}.in"
    with open(f"data_solutions/{case}.out", 'r') as input_file:
        correct_answer = ''.join(input_file.readlines())
        formatted_correct_answer = correct_answer.replace("\n", ' ')
        print(f"For file {input_file_name} the correct answer is {formatted_correct_answer}")
        print(f"Working on {input_file_name}")
        your_answer = determine_solution(input_file_name)
        if correct_answer != your_answer:
            formatted_your_answer = your_answer.replace("\n", " ")
            print(f"Your answer of {formatted_your_answer} is not correct, try again.")
            exit()
