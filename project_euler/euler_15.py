# https://projecteuler.net/problem=15

# Starting in the top left corner of a 2x2 grid, and only being able to move to the right
# and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20x20 grid?

# Replace the below with your program.
def findRoutes(lefts, rights, mem={}):
    if (lefts, rights) in mem:
        return mem[(lefts, rights)]
    if lefts==0 or rights==0:
        return 1
    mem[(lefts, rights)] = findRoutes(lefts-1, rights)+findRoutes(lefts, rights-1)
    return mem[(lefts, rights)]
print(findRoutes(20, 20))
