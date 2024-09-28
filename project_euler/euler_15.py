# https://projecteuler.net/problem=15

# Starting in the top left corner of a 2x2 grid, and only being able to move to the right
# and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20x20 grid?

# Replace the below with your program.
def findRoutes(remainingLefts, remainingRights):
    if remainingLefts == 0:
        return 1
    if remainingRights == 0:
        return 1
    return findRoutes(remainingLefts-1, remainingRights)+findRoutes(remainingLefts, remainingRights-1)

print(findRoutes(20, 20))
