# 1. Using the print() function, print out 'Hello World!'
print("Hello World!")
# 2. Print a number and then print an empty line.
print("123\n")
# 3. Print out variables, both numbers and strings.  Add an extra empty line.
number_1 = 2
number_2 = 4
number_3 = 1.946
name = "Allanna"
greeting = "Hello, "
print(number_1)
print("\n")
# 4. Print two the greeting and the name together on the same line. It should print 'Hello, Allanna'
# Also, try it with an exclamation pint added to the end of the line.
print(greeting+name+"!")
# 5. Print a number and a string together. It could print, for example, 'Hello, 5'. You can also try
# printing both variables without using concatenation, as additional arguments to print()
print("Hello, 5")
# 6. Create a list of numbers from 0 to 5
numbersfrom0to5=[]
for i in range(1, 6):
    numbersfrom0to5.append(i)
print(numbersfrom0to5)
# 7. Create a list from number_1, number_2, and number_3
listwith3numbers=[number_1, number_2, number_3]
# 8. Print out the whole list and each of the three numbers in the list you created, each on their
# own line.
print(listwith3numbers)
print(listwith3numbers[0])
print(listwith3numbers[1])
print(listwith3numbers[2])
# 9. Have the program prompt for a name.
name=input("What is your name? ")
# 10. Print out that name with a greeting, e.g. 'Hello Xander!' if the user enters Xander.
print(f"Hello {name}!")
# 11. Ask the first name and last name of the user, then print a custom greeting.
firstname=input("What is your first name? ")
lastname=input("What is your last name? ")
print(f"Hello {firstname} {lastname}!")
# 12. Ask the user for two numbers, and the print the sum of those two numbers.
number_1=input("Enter a number: ")
number_2=input("Enter a number: ")
print(f"{number_1} plus {number_2} equals {int(number_1)+int(number_2)}")
# 13. Read a line of numbers, use the split() function to separate them into an array, and then print
# them.
numbers=input("Enter some numbers! ")
numbers=str(numbers)
numbersarray=[]
for x in range(len(numbers)):
    numbersarray.append(int(numbers[0]))
    numbers=numbers[1:]
print(numbersarray)
# 14. For the array of numbers generated in step 13, print out each element times 2.
for z in range(len(numbersarray)):
    print(2*int(numbersarray[z]))