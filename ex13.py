"""
In this program we're gonna use sys module, and using argv function to take all the arguments that we pass when execute the script.
And and this program, if we passed argument less than the variables we define, it'll give us an error output, because the program need to unpack
the arguments into defined variables. 
"""

from sys import argv

script, first, second, third = argv

print("The script is called", script)
print("Your first variable is", first)
print("Your second variable is", second)
print("Your third variable is", third)

print(argv[0])
