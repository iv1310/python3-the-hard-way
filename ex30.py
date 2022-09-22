people = 30
cars = 40
trucks = 15

# Compare if the cars is greater than people, then print a string.
if cars > people:
    print("We should take the cars.")
# Go to another conditional which cars is less than people, then print a string.
# And if we have multiple elif that has True value, then it only print the first block that is True, so it will run only the first one.
elif cars < people:
    print("We should not take the cars.")
# Go to this confitional if nothing in the above conditional match with the condition, then print a string.
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
