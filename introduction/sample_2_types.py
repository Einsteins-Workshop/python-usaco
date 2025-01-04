# Different types can have different operations performed on them.

number_four = 4
print("This is the result of adding two number fours")
print(number_four + number_four)
print(8 + 9)

string_four = "4"
print("This is the result of adding two string fours")
print(string_four + string_four)
print("abc" + "def")

# Note that you cannot "add" a string and a number.  You can convert between strings and numbers
# using the str() and int() functions.
print(int("100") + 11)

print("This is the number:" + str(4))
# The int() function is particularly useful for trying to use input() to get a number from the user
# as input() always returns a string
number_as_a_string = input("Enter a number\n")
number = int(number_as_a_string)
print("Double that number is:")
print(number + number)

# Also note in the input function of the prior example the "\n" in the string. This represents
# a new line.

