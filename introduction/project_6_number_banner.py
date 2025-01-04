# Print the following pattern, with each line containing 10 numbers:
# 1234567890
# 0123456789
# 9012345678
# 8901234567
# 7890123456
# 6789012345
# 5678901234
# 4567890123
# 3456789012

# Use two loops for this, one for each line,
# and one loop to construct the ten number string to print.

# You may want to start with printing with two loops:

# 1111111111
# 2222222222
# 3333333333
# 4444444444
# 5555555555
# 6666666666
# 7777777777
# 8888888888
# 9999999999

# Here is a sample an example of printing the above simpler banner:
for i in range (1, 10):
    line_to_print = ''
    for j in range (0, 9):
        line_to_print += str(i)
    print(line_to_print)