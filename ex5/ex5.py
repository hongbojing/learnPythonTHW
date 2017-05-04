name = 'Hongbo Jing'
age = 28 # not a lie
height = 70 # inches
height_in_cm = height * 2.54
weight = 165 # lbs
weight_in_kg = weight * 0.453592
eyes = 'Black'
teeth = 'White'
hair = 'Black'

# I change name to age, and I got "Let's talk about 28, lol"
print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "That's %d cm tall." %height_in_cm
print "He's %d pounds heavy." % weight
print "And that's %d in kg." % weight_in_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
