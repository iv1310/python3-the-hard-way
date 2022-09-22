"""
There are three ways we can call range():
    1. range(stop) --> take one argument.
        => When user call range() with one argument, user will get a series of numbers that start at 0 and include every whole number up to, but not including, the 
            number that user have provided as the stop.
    2. range(start, stop) --> takes two arguments.
        => When user call range() with two arguments, user get to decide not only where the series of numbers stops but also where it starts, so user don't have 
            to start at 0 all the time.
    3. range*start, stop, step) --> takes three arguments.
        => When user call range() with three arguments, the user can choose not only where the series of numbers will start and stop but also how big the difference 
            will be between one number and the next.

Points to remember about python range() function:
    1. range() function only work with the integers, i.e. whole numbers.
    2. All arguments must be integers.
    3. All three arguments can be positive or negative.
    4. The step value must not be zero.
    5. range() is a type in python.
    6. Users can access items in a range() by index, just as users do with a list.
"""

# printing a number
for i in range(10):
    print(i, end=' ')
print()

# using range for iteration
l = [10, 20, 30, 40]
for i in range(len(l)):
    print(l[i], end=' ')
print()

# performing sum of natural number
sum = 0
for i in range(1, 11):
    sum += i
print(f"Sum of first 10 natural number: {sum}")


# using range to print number divisible by 3
for i in range(0, 30, 3):
    print(i, end=' ')
print()

# using range to print number divisible by 5
for i in range(0, 50, 5):
    print(i, end=' ')
print()


# Incremented by -2
for i in range(25, 2, -2):
    print(i, end=' ')
print()

# incremented by -3
for i in range(25, -6, -3):
    print(i, end=' ')
print()

# accessing range() with index value.
ele = range(10)[0]
print("First element:", ele)

ele = range(10)[-1]
print(f"\nLast element: {ele}")

ele = range(10)[4]
print("\nFifth element: {}".format(ele))
