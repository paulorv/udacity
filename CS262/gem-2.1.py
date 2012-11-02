# Bonus Practice: Find Max

# This assignment is not graded and we encourage you to experiment. Learning is
# fun!

# Given a list l and a function f, return the element of l that maximizes f.

# Assume:
#    l is not empty
#    f returns a number

import math

def max(l,f):
	maximum = None
	for i in l:
		if f(i) > f(maximum):
			maximum = i
	return maximum


# Example:

l = ['Barbara', 'kingsolver', 'wrote', 'The', 'Poisonwood','Bible']
f = len
print max(l,f)


l = [16, 25, 4, 1]
f = math.sqrt
print max(l,f)

# Try it on your own!
