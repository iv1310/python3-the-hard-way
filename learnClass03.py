class Dog:

    # a simple class attributes
    attr1 = "mammal"
    attr2 = "dog"

    # a sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)

# Driver code
# Object instantiation
Rodger = Dog()

# accessing class attributes
# and method through object
print(Rodger.attr1)
Rodger.fun()
