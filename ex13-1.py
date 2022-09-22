"""
The difference between input() and sys.argv is if they give your script inputs on the command line, then you use sys.argv.
If you want them to input using the keyboard while the script is running, then use input().
"""

from sys import argv

script, first, second = argv

print(f"The file named is {script}, and here {first} is the first argument, and here {second} is the second argument.")

# Input will convert the variable or data that had been typed into a string, but if we wanted to converted it or used it as an integer, use int(input()).
age = int(input("Please tell us your age? "))
print(age)
