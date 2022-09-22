class Dog:

    # class variable
    animal = 'dog'

    # the init method or constructor
    def __init__(self, breed, color):
        # instance variables
        self.breed = breed
        self.color = color

# Object of dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed:', Rodger.breed)
print('Color:', Rodger.color)

print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed:', Buzo.breed)
print('Color:', Buzo.color)

# Class variables can be accessed using class name also
print('\nAccessing class variable using class name')
print(Dog.animal)
