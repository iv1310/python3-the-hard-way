# Create a variable named cars and assigned integer 100 to it.
cars = 100

# Create a variable named space_in_a_car and assigned floating point 4.0 to it.
space_in_a_car = 4.0

# Create a variable named drivers and assigned integer 30 to it.
drivers = 30

# Create a variable named passengers and assigned integer 90 to it.
passengers = 90

# Create a variable named cars_not_driven and assigned the value of cars - drivers.
cars_not_driven = cars - drivers

# Create a variable named cars_driven and assigned the value of variable drivers 
cars_driven = drivers

# Create a variable named carpool_capacity and assigned the value of cars_driven * space_in_a_car, and the value will be a floating point.
carpool_capacity = cars_driven * space_in_a_car

# Create a variable named average_passengers_per_car and assigned the value of passengers / cars_driven, and the value will be a floating point because it use ('/') to divide.
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")
