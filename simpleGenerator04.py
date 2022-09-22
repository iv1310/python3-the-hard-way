# This Python program is to find the series of fibonacci numbers.
def fibonacci(n):
    # The fibonacci is the series of numbers that adding up the two number before it.
    # 0,1, and the next number is 0 + 1, so the third number is 1, and the fourth number is 1 + 1 = 2.
    x, y = 0, 1
    total = 0
    while total < n:
        yield x
        z = x + y
        x = y
        y = z
        total += 1

print(list(fibonacci(20)))
