# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built in functions.

# def biggest(i,j,k):
#     if i > j and i > k:
#         return i
#     else:
#         if j > i and j > k:
#             return j
#         else:
#             return k


def set_range(i,j,k):
    return max(i,j,k) - min(i,j,k)


print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6

print set_range(1.1, 7.4, 18.7)
#>>> 17.6 # since 18.7 - 1.1 = 17.6