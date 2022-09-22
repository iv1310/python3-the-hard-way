# Import function argv from module sys
from sys import argv

# Unpack the arguments that has been passed while executing the script into variables.
script, filename = argv

# Using the function `open` to literally open a file, and assign it to variable txt.
txt = open(filename)

# Print string with formatted to pass the variable into that string.
print(f"Here's your file {filename}.")
# Using function `read` to read the content of file inside the function open and print it.
print(txt.read())
txt.close()

# Print a string
print("Type the filename again.")
# Using function input to get the input from the prompt and passed it variable.
file_again = input("> ")

# Using the function `open` to literally open a file, and assign it to variable txt.
txt_again = open(file_again)

# Using function `read` to read the content of file inside the function open and print it.
print(txt_again.read())
txt_again.close()
