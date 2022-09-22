def filterOdd(numbers):
    for number in range(numbers):
        if(number % 2 != 0):
            yield number

oddNumbers = filterOdd(20)

# Another method to print the elements stored inside a generator object is using the next() method. 
# Each time we invoke the next() method on the generator object, it returns the next item.
print(next(oddNumbers))
print(next(oddNumbers))
print(next(oddNumbers))
print(next(oddNumbers))

print(f"The output as a list : {list(oddNumbers)}")

