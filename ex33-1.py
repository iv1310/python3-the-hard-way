i = 0
numbers = []

limits = int(input("Enter the limit of the loop? "))

while i < limits:
    print(f"At the top i is {i}")
    numbers.append(i)
    i += 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}\n")

print("The numbers: ")

for num in numbers:
    print(num, end=' ')
