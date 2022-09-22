limits = int(input("Enter the limit of the loop? "))

def addList(num):
    i = 0
    numbers = []
    while i < num:
        print(f"At the top i is {i}")
        numbers.append(i)
        i += 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}\n")
    return numbers

print("The numbers: ")

for num in addList(limits):
    print(num, end=' ')
