# TODO: Convert the 'what' script to a 'normal' formula.
# TODO: Modify for practice.

# Add Function
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

# Subtract Function
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

# Multiply Function
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

# Divide Function
def divide(a, b):
    print "DIVING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

# Sets variables that calls functions with set parameters.
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
