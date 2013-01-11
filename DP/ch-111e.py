# Write a function that, given a string, removes from the string any * character,
# or any character that's one to the left or one to the right of a * character.
#
# Examples:
# "adf*lp" --> "adp"
# "a*o" --> ""
# "*dech*" --> "ec"
# "de**po" --> "do"
# "sa*n*ti" --> "si"
# "abc" --> "abc"

def star_delete(star_string):
	new_string = ""
	for i in star_string:
		if i == "*":
			
	return new_string


star_string = "*Star*"
print star_delete(star_string)
