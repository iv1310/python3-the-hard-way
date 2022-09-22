class Animal(object):
    def __init__(self, animal_type):
        print("Animal type:", animal_type)

class Mammal(Animal):
    def __init__(self):
        # call superclass
        super().__init__('Mammal')
        print("Mammal give birth directly.")

dog = Mammal()
