# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

# While-loop method
def make_hashtable(nbuckets):
	h = []
	n = 0
	while n < nbuckets:
		h.append([])
		n += 1
	return h


# For-loop method
def make_hashtable_for(nbuckets):
	table = []
	for unused in range(0,nbuckets):
		table.append([])
	return table
	

print make_hashtable(12)
