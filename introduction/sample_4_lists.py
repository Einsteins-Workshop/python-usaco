#Lists are a sequence of objects, and are created by putting items inside []
my_list = [1,4,6,8]
# You can add things to a list with the append method.
my_list.append(7)
#You can look at elements of the list my_list[1]. Indexes are tricky, starting at 0. Y
# ou can also use negative index elements, which count from the end of the list.
# Create a list and try accessing elements of the list:
print(my_list[0])
print(my_list[2])
print(my_list[-1])

# Note that lists can contain anything. They can contain numbers and strings together, or even other
# lists!
complex_list = [1, 2, "a", "b", [1, 2, 3]]
print(complex_list)
print(complex_list[0])
print(complex_list[-1][2])

# You can also change elements of the list like they are variables
my_list[0] = "Changed"
print(my_list)

# You can get a range of values, creating a new list, using [:] notation
print(my_list[1:3]) # This will get everything from position 1 (the second index) up to but not
                    # including position 3. So, it will print out two elements.

# You can also use the range() function to quickly get a list of numbers from 0 to one less than the
# argument
print(list(range(10)))