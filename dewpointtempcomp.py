from mysci.readdata import read_data
from mysci.printing import print_comparison
from mysci.computation import compute_dewpoint

# Column names and column indices to read
columns = {'date': 0, 'time': 1, 'tempout': 2, 'humout': 5, 'dewpt': 6}

# Data types for each column (only if non-string)
types = {'tempout': float, 'humout': float, 'dewpt': float}

# Read data from file
data = read_data(columns, types=types)

# Compute the wind chill factor
dewpoint = [compute_dewpoint(t, h) for t, h in zip(data['tempout'], data['humout'])]

# Output comparison of data
print_comparison('DEW POINT', data['date'], data['time'], data['dewpt'], dewpoint)