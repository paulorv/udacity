# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(p):
	greatest = 0
	for i in p:
		if i > greatest:
			greatest = i
	return greatest




print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

    
