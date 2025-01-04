# Variables can be set to values using =.
age = 10

# Strings are what python calls words. To create a new one, you have to put them within either
# double quotes ("") or single quotes('')
pet_name = "Fido"

# To print something to the console, use the print function.
print("Hello World!")
print(age)
print(pet_name)

# To get input from the user from the console, use the input function. You can include
# a prompt, as an argument, to the function.
name = input("Please enter your first name.")

# Strings can be combined using either + (the concatenation operator), or using string interperolation
# using f"" templates.

print("Hello " + name + "!")
last_name = input("Please enter your last name.")

print(f"Your full name is {name} {last_name}.")