## Animal is-a object.
class Animal(object):
    def __init__(self):
        print("Animal is a good creature.")

    def who():
        print("Animal is...")

## Make a class named Dog that is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ## Dog has-a instance attribute named name
        self.name = name

## Make a class named Cat that is-a Animal
class Cat(Animal):
    def __init__(self, name):
        ## Cat has-a instance attribute named name
        self.name = name

## Make a class named Person that is-a object
class Person(object):
    def __init__(self, name):
        ## Person has-a instance attribute named name
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## Make a class named Employee that is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        ## 
        super(Employee, self).__init__(name)
        ## Employee has-a instance attribute named salary
        self.salary = salary

## Make a class named Fish that is-a object
class Fish(object):
    pass

## Make a class named Salmon that is-a Fish
class Salmon(Fish):
    pass

## Make a class named Halibut that is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")
rover.who()

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet attribute and set it to satan
mary.pet = satan

## frank is-a Employee with attribute salary
frank = Employee("Frank", 120000)

## frank has-a pet attribute and set it to rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
