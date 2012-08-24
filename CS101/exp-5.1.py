# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a' 
# following 'z'.

def shift(letter):
	alpha_len = 26
	n = 1
	shift = chr(ord(letter) + n)
	if ord(shift) >= (ord('a') + alpha_len):
		shift = chr(ord(letter) + n - alpha_len)
	return shift
		
	# if letter == 'z':
	# 	return chr(ord(letter) - 25)
	# return chr(ord(letter) + 2)



print shift('a')
#>>> b
print shift('n')
#>>> o
print shift('z')
#>>> a