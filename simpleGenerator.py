# A generator function that yields 1 for the first time, 2 second time, and 3 third time.

def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

# Driver code to check above generator function
for i in simpleGeneratorFun():
    print(i)

"""
The execution of generator function starts only when the caller iterates over the generator object. Hence, it increases the overall efficiency of the program
along with decreasing memory consumption. Some situations where we should use yield are:
1. When the size of returned data is quite large, instead of storing them into list, we can use yield.
2. If we want to faster execution or computation over large datasets, yield is a better option.
3. If we want to reduce memory consumption, we can use yield.
4. It can be used to produce an infinite stream of data. We can set the size of a list to infinite, as it might cause a memory limit error.
5. If we want to make continuous calls to a function that contains a yield statement, it starts from the last defined yield statement, and hence,
    we can save a lot of time.
"""
