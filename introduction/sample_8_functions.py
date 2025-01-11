# In addition to the existing input() and print() functions, you can make your own. They are useful
# in a way similar to for loops and while loops, as a way to reuse code. However, they are even more
# flexible in how you call them and use them later.

# Functions are created using the def keyword.

def hello_function():
    print("Hello World!")

print("Trying out hello function")
# We cal our new function similar to
hello_function()

# We can also have our function take arguments
def greet(first_name, last_name):
    print("Hello " + first_name + ' ' + last_name)
greet("Albert", "Einstein") # Note that we need to call the function with all arguments
greet("Taylor", "Swift")
# We can also send arguments with a dictionary-like key/value syntax
greet(first_name="Nelson", last_name="Mandela")

# Functions can return a value using the return statement. Note that the return statement stops further
# use of the function
def absolute_value(number):
    if number > 0:
        return number
    return -1 * number

print(absolute_value(10))
print(absolute_value(-4))

# Functions can also be recursive, calling themselves. Though you need to be careful that you don't
# create an infinite loop, recursion can be a powerful tool to solve otherwise hard to solve problems.
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(f"The tenth Fibonacci number is {fibonacci(10)}")