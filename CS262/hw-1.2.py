import re

def sumnums(sentence): 
# write your code here
	found = re.findall("[0-9]+", sentence)
	if len(found) > 0:
		found = [int(i) for i in found]
		sumints = sum(found)
		return sumints
	else:
		return 0
		
	#print type(found)
	# for i in found:
	# 	print i
	# 	print type(i)
	

	# another way (str > int)
	# found = map(int, found)
         
sumnums("8 planets and 4 moons")
        
# This problem includes an example test case to help you tell if you are on
# the right track. You may want to make your own additional tests as well.

test_case_input = """The Act of Independence of Lithuania was signed 
on February 16, 1918, by 20 council members."""

test_case_output = 1954

if sumnums(test_case_input) == test_case_output:
  print "Test case passed."
else:
  print "Test case failed:" 
  print sumnums(test_case_input) 
