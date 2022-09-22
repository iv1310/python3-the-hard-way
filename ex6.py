# Create a variable named types_of_people and assigned integer as the value and the value is 10.
types_of_people = 10
# Create a variable named x and assigned strings as the value and inside the string also will refer to another variable(types_of_people).
x = f"There are {types_of_people} types of people."

# Create a variable named binary and assigned string as the value.
binary = "binary"
# Create a variable named do_not and assigned string as the value.
do_not = "don't"
# Create a variable named y and assigned strings as the value and inside the string also will refer to another variables(binary and do_not).
y = f"Those who know {binary} and those who {do_not}"

# Print the variable x as a string
print(x)
# Print the variable y as a string
print(y)

# Print the string that has a string inside it as a variable.
print(f"I said: {x}")
# Print the string that has a string inside it as a variable.
print(f"I also said: '{y}'")

# Create a variable named hilarious and assigned boolean as the value.
hilarious = False
# Create a variable named joke_evaluation and assigned string as the value with a format to refer to a variable.
joke_evaluation = "Isn't that joke so funny? {}"

# Print the variable joke_evaluation with format to add a variable inside the string.
print(joke_evaluation.format(hilarious))

test = "apa"
tust = 14
tist = 3.14
tost = True
print("{} yang menjadi pertanyaan nomor {} dan nilai dari PI adalah {} yakan? {}".format(test, tust, tist, tost))

# Create a variable named w and assigned string as the value.
w = "This is the left side of...."
# Create a variable named e and assigned string as the value.
e = "a string with a right side."

# Print the string from variable w and e, and concate both variable into a full strings.
print(w + e)
