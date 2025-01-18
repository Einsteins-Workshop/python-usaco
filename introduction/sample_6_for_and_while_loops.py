# Loops are useful for repeating the same code multiple times. Some of the simplest loops
# are those that iterate over a list. In these, a loop variable takes on the value of each
# element of the list.

# This will print out each of the four primes, one at a time.
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# You can use the range function to quickly enumerate the numbers starting from 0.

# This will print out the numbers 0, 1, 2, 3, and 4
for x in range(5):
    print(x)

# You can use enumerate to get the current index of the list for that array element
l1 = ["eat", "sleep", "repeat"]

# The following will print the following on separate lines: 0, "eat", 1, "sleep", 2, "repeat"
for count, verb in enumerate(l1):
    print(count)
    print(verb)

# Loops can also be made with while loops, which will keep running as long a s acondition is
# satisfied.

# This will run as long as the number is less than 50, so will print 0, 10, 20, 30, 40
number = 0
while number < 50:
    print(number)
    number = number + 10

# We can also use this construction to keep asking the user for an input
user_input = "y"
while user_input == "y":     # Note the ==.  This is how we check two things are equal. One = would set
                             # the value instead.
    user_input = input("Please enter y to keep looping\n")

# You can use break to get out of a loop (either for loop or while loop)
while True:
    user_input = input("Please enter n to leave loop\n")
    if user_input == "n":
        break

# You can use continue to skip a particular run of a loop
for i in range(20):
    # Skip all numbers divisible by 2 or 3
    if (i % 2 == 0) or (i % 3 == 0):
        continue
    print(i)

