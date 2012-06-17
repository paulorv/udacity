# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a' 
# following 'z'.

def shift(letter):
	wildcard = 0
	shifted = ord(letter) - wildcard
	if ord(letter) >= ord('z'):
		wildcard = 25
		return chr(shifted)
	return chr(shifted + 1)
		
	# if letter == 'z':
	# 	return chr(ord(letter) - 25)
	# return chr(ord(letter) + 1)



print shift('a')
#>>> b
print shift('n')
#>>> o
print shift('z')
#>>> a