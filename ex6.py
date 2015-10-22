# Variables to be used for print function
x = "There are %d types of people." % 10    # decimal modulo for string
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # multiple modulus

# Calls the print function using set variables
print x
print y

# Print functions using previously used modulus variables above
print "I said: %r." % x
print "I also said: '%s'." % y

# Set boolean to variable for modulo below
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

# Set variables to be used for string concatenation below.
w = "This is the left side of..."
e = "a string with a right side."

print w + e
