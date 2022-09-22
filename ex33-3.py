import sys

limits = int(input("Enter the limit of the loop? "))
diff = int(input("Enter how much it will increase per loop? "))

if diff > limits:
    print("\nThe diff is bigger than the limits!!\n")
    sys.exit()

def addList(diff, num):
    i = 0
    numbers = []
    while i < num:
        print(f"At the top i is {i}")
        numbers.append(i)
        i += diff
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}\n")
    return numbers

print("The numbers: ")

for num in addList(diff, limits):
    print(num, end=' ')
