class Dog:
    # class variable
    animal = 'dog'

    # the init method or constructor
    def __init__(self, breed):
        # instance variable
        self.breed = breed

    # add an instance variable
    def setColor(self, color):
        self.color = color

    # retrieve instance variable
    def getColor(self):
        return self.color

# Driver code
Rodger = Dog("pug") 
Rodger.setColor("brown")
print(Rodger.getColor())
