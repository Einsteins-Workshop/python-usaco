# For conditions, there are the ==, > , >=, <, <= operators. You can use "and" and "or"
# to combine conditions and not to negate

# You can combine this with the if clause to sometimes run a block of commands
number = int(input("Enter a number\n"))

if number > 100:
    print("Your number is greater than 100.")

if number == 10:
    print("Your number is 10")

if not(number == 3):
    print("Your number is not 3")

if (number % 3 == 0) or (number %2 == 0):
    print("Your number is divisible by either 2 or 3")

# Multiple if statements can be chained with elif and a default clause can be added with else.
# Note that once part of an if/elif chain is matched, the rest will be ignored.

age = int(input("How old are you?\n"))
if age > 90:
    print("You are too old to party, grandpa.")
elif age < 0:
    print("You're not yet born.")
elif age >= 18:
    print("You are allowed to party.")
else:
    print("You are too young to party.")