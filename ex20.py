# Using function argv to take the arguments while executing the script from module sys
from sys import argv

# Unpack the given arguments into variables.
script, input_file = argv

# a function with named print_all, it has parameter called f, and it will print content of a file/
def print_all(f):
    print(f.read())

# a function with named rewind, it has paramter called f, and it will change the position of file into 0(bytes).
def rewind(f):
    f.seek(0)

# a function with named print_a_line, it has 2 paramters called line_count and f, and it will print the content of file per line.
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Open the file named input_file, and it will be a file object, so we can move around inside it.
current_file = open(input_file, "r")

print("First let's print the whole line.")
# use to call the function named print_all and assign variable current_file into the function as an argument.
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# use to call the function named rewind and assign variable current_file into the function as an argument.
rewind(current_file)

print("Let's print three lines.")

# assign number 1 into variable current_line
current_line = 1
# use to call the function named print_a_line and assign variables current_line and current_file into the function as arguments.
print_a_line(current_line, current_file)

# Increment the value of current_line with 1.
current_line = current_line + 1
# use to call the function named print_a_line and assign variables current_line and current_file into the function as arguments.
print_a_line(current_line, current_file)

# Increment the value of current_line with 1.
current_line = current_line + 1
# use to call the function named print_a_line and assign variables current_line and current_file into the function as arguments.
print_a_line(current_line, current_file)
