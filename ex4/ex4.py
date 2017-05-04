# Define and assign valeus to the other variables
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

# Use the variables defined above, and do some meaningful calculation.
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# Print some sentences with some prepared numbers in them.
# Remember to use comma to divide the content.
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Try to print without spaces between words in print.
print "Hey %s there." % "you are good"
