# Read the data file
filename = 'data/wxobs20170821.txt'

# This is a "context manager" - considered a best practice in opening files because it closes the datafile after
# reading. Use readline to see the header.
with open(filename, 'r') as datafile:
    data = datafile.read()
