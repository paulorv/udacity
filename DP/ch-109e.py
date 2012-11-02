# Description:
# Write a function, where given a string, return true if it only contains the digits from 0 (zero) to 9 (nine). 
# Else, return false.
#
# Input Description:
# string data - a given string that may or may not contains digits; will never be empty
#
# Output Description:
# Return True or False - true if the given string only contains digits, false otherwise
#
# Sample Inputs & Outputs:
# "123" should return true. "123.123" should return a false. "abc" should return a false.
#
# Notes:
# This is a trivial programming exercise, but a real challenge would be to optimize this function
# for your language and/or environment. As a recommended reading, look into how fast string-searching works.

import re

# RegEx Solution (Long)
def digits_regex1(s):
	if len(data) > 0:
		if re.match(r"^\d+$",data):
			return True
		return False
	return False

# RegEx Solution (Short)
def digits_regex2(s):
	return re.match(r"^\d+$",s) != None

#Recursive Solution
def digits_rec(s):
	if s == '':
		return True
	else:
		return s[0] in '1234567890' and digits_rec(s[1:])


data = "232323424240"
print digits_regex1(data)
print digits_regex2(data)
print digits_rec(data)
