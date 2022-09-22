# Create a variable named formatter and assigned a string as the value.
formatter = "{} {} {} {}"

# Print the variable as a string
print(formatter)

# Print the variable but use the format function to references the tuples {} with some integer values.
print(formatter.format(1, 2, 3, 4))

# Print the variable but use the format function to references the tuples {} with some string values.
print(formatter.format("one", "two", "three", "four"))

# Print the variable but use the format function to references the tuples {} with some boolean values.
print(formatter.format(True, False, False, True))

# Print the variable but use the format function to references the tuples {} with the value the variable it self, so it will multiple 4 times.
print(formatter.format(formatter, formatter, formatter, formatter))

# Print the variable but use the format function to references the tuples {} with some string values.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear",
    "How about this one"
))
