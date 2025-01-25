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
    gimmiefiles = open(file_name, "r")

    looplimit = gimmiefiles.readline().rstrip()
    cows = gimmiefiles.readline().rstrip()
    canes = gimmiefiles.readline().rstrip()

    looplimit = [int(x) for x in looplimit.split(" ")]
    cows = [int(x) for x in cows.split(" ")]
    canes = [int(x) for x in canes.split(" ")]

    del looplimit[0]
    looplimit = looplimit[0]
    for x in range(looplimit):
        curcanehei = [0, canes.pop(0)]
        for (i, cow) in enumerate(cows):
            if cows[i] > curcanehei[0]:
                if cows[i] > curcanehei[1]:
                    cows[i] = cows[i] + curcanehei[1] - curcanehei[0]
                    curcanehei[0] = curcanehei[1]
                else:
                    cowtemp = cows[i]
                    cows[i] = cows[i] * 2 - curcanehei[0]
                    curcanehei[0] = cowtemp

    cows = [str(x) for x in cows]
    printernullvoidpublicstaticvoidmain = "\n".join(cows) + "\n"
    print(printernullvoidpublicstaticvoidmain)
    return (printernullvoidpublicstaticvoidmain)
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
