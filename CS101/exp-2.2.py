def stamps(n):
    if n % 5 != 0:
		if (n % 5) % 2 != 0:
			return "(" + str(n/5) + ", " + str((n%5)/2) + ", " + str((n%5)%2) + ")"
		else:
			return "(" + str(n/5) + ", " + str((n%5)/2) + ", 0)"
    else:
        return "(" + str(n/5) + ", 0, 0)"


print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and one 1p stamp
print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps