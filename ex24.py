print("Let's practice everything.")
# Print a string with escape character \
print('You\'d need to know \'bout espaces what \\ that do:')
# Print a string with escape sequences \n for newline and \t for tabs
print('\n newlines and \t tabs.')

# Create a variable with multi-line string
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("-----------------------")
# Print the variable with multi-line strings
print(poem)
print("-----------------------")


five = 10 - 2 + 3 - 6
# Print a format string with variable five
print(f"This should be five: {five}")

# Create a function named secret_formula and it has 1 argument named started, and it will calculated some values and stores it on some variables, then return 
# the 3 variables as a list of integer.
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
# Unpack the variables from the function and stored it to the defined variables.
beans, jars, crates = secret_formula(start_point)

# Remember this another way to format a string.
print("With a starting point of: {}".format(start_point))
# It's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates")

start_point = start_point / 10

print("We can also do that this way: ")
# Store the variable(a list of integer) from function into a new variable named formula.
formula = secret_formula(start_point)
print(type(formula))
# This is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
