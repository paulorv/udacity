#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
	count = 0
	s = 0
	t = 1
	while t < n:
		t = s + t
		s = t
		print t
		count += 1





print fibonacci(36)
#>>> 14930352
