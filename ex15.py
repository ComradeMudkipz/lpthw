# Refer to pydoc open for further info with open().
# TODO: Review the use of raw_input().
from sys import argv

# Sets argument variable.
script, filename = argv

# Sets filename argument to var and opens inputted file.
txt = open(filename)

# Prints the filename and reads to text mode.
print "Here's your file %r:" % filename
print txt.read()
txt.close()

# Prompts user to type the same filename to confirm.
## print "Type the filename again:"
## file_again = raw_input("> ")

# Opens previous file.
## txt_again = open(file_again)

# Reads previous file.
## print txt_again.read()
