class Dog:
    # class attribute
    attr1 = "mammal"

    # instance attribute
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))

# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# accessing class method
Rodger.speak()
Tommy.speak()
