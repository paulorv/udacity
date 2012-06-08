# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

index = [['This', ['fake.text']], ['is', ['real.text']], ['a', ['fake.text']], ['test', ['real.text']]]


def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
	
	i = 0
	# Index breaking approach
	keywords = content.split()
	for kword in keywords:
		for entry in index:
			if kword == entry[0] and url not in entry[1]:
				entry[1].append(url)
		# if kword in index[i]:
		# 	print "Match"
		# 	i = i + 1
			
				# entry[1].append(url)
				# print "URL added for entry '" + entry[0] + "' : " + entry[1][1]
		# if entry[0] not in keywords:
		# 			print entry[0]
		
	
	
	# keywords = content.split()
	# for entry in index:
	# 	i = 0
	# 	if entry[i] not in keywords:
	# 		
	# 	if entry[i] in keywords:
	# 		entry[1].append(url)
	# 		i = i + 1
	
	# i = 0
	# for keyword in keywords:
	# 	if keyword in index[i]:
	# 		print index[i]
	# 		i = i + 1
		# entry.append(content.split())




print add_page_to_index(index,'real.text',"This is a test")
print index
#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>> ['test',['fake.text']]]


