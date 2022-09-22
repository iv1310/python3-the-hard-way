# A Python program to generate squares from 1 to 100 using yield and therefore generator.

# An infinite generator function that prints next square number. It starts with 1.

def nextSquare():
    i = 1

    # An infinite loop to generate squares
    while True:
        yield i*i
        i += 1 # Next execution resumes from this point

# Driver code to test above generator function
for num in nextSquare():
    if num > 100:
        break
    print(num)

"""
When you call a function that has a yield statement, as soon as a yield is encountered, the execution of the function stops, and 
returns an object of the generator to the function caller. If you want to get the values stored inside the generator object, you need to iterate over it.
"""
