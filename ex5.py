name = 'Joshua B. Ongtawco'
age = 20 # not a lie
height = 74.0 # inches
height_cm = height * 2.54
weight = 200.0 # lbs
weight_kg = weight / 2.2046
eyes = 'Brown'
teeth = 'White'
hair = 'Dark brown'

print "Let's talk about %r." % name
print "He's %d centimeters tall." % height_cm
print "He's %d kilograms fat." % weight_kg
print "He's pretty damn fat."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height_cm, weight_kg, age + height_cm + weight_kg)
