# Insted of return values using yield, you can call functions. 

def cubes(number):
    return number*number*number

def getCubes(n):
    for i in range(n):
        yield cubes(i)

cubeObject = getCubes(5)
print(list(cubeObject))
