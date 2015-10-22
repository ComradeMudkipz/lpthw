# TODO: Convert while loop to a function that can be called.
# TODO: Replace '6' in 'i < 6' to a variable
# TODO: Add variable to the function that could change '+ 1'
#       on line 8 to change increments.
# TODO: Refer to study drill 5.

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num
