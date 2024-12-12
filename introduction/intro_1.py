# See https://pyflo.net/print/
# https://pyflo.net/more-printing/
# https://pyflo.net/variables/
# https://pyflo.net/input/
# https://pyflo.net/integers/
# https://pyflo.net/string-multiplication/
# https://pyflo.net/lists/
# 1. Using the print() function, print out 'Hello World!'
print('Hello World!')
# 2. Print a number and then print an empty line.
print(1)
print('\n')
# 3. Print out variables, both numbers and strings.  Add an extra empty line.
number_1 = 2
number_2 = 4
number_3 = 1.946
name = "Allanna!"
greeting = "Hello,"
print(number_1)
print(number_2)
print(number_3)
print(name)
print(greeting)
print('\n')
# 4. Print two the greeting and the name together on the same line. It should print 'Hello, Allanna'
# Also, try it with an exclamation pint added to the end of the line.
print(greeting,name)

print(None)
Hoi = ['banana','ono','chop','fire']
print(Hoi[2])
Hoi[2] = 'water'
print(Hoi[2])

# 5. Print a number and a string together. It could print, for example, 'Hello, 5'. You can also try
# printing both variables without using concatenation, as additional arguments to print()
#
print('Hello, 5')
print('Hello,')
print('5')
# 6. Create a list of numbers from 0 to 5
print('012345')
# 7. Create a list from number_1, number_2, and number_3

thislist = [number_1,number_2,number_3]
print(thislist)#in the list you created, each on their
# own line.
print(2)
print(4)
print(1.946)
# 9. Have the program prompt for a name.
name = input('What is your name?')

# 10. Print out that name with a greeting, e.g. 'Hello Xander!' if the user enters Xander.
print('Hello,'+name)
# 11. Ask the first name and last name of the user, then print a custom greeting.
first = input('What is your first name?')
last = input('What is your last name?')
print('Hello,'+first+last)
# 12. Ask the user for two numbers, and the print the sum of those two numbers.
num = input('Can you tell me one number?')
number = input('Can you tell me another number?')
true_num = int(num)
true_number = int(number)
print(true_num+true_number)
# 13. Read a line of numbers, use the split() function to separate them into an array, and then print
# them.
mynums = input('Tell me a line of numbers separated by spaces.')
x = mynums.split()
print(x)
# 14. For the array of numbers generated in step 13, print out each element times 2.
primes = [mynums]
for prime in x:
    print(int(prime)*2)

