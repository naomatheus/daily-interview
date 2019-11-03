# This problem was recently asked by Facebook.

# Kaprekar's Constant is the number 6174.
# This number is special because it has the property where for any 4-digit number that has 2 or more unique digits, if you repeatedly apply a certain function it always reaches the number 6174.

# This certain function is as follows:
# - Order the number in ascending form, and descending form to create 2 numbers.
# - Pad the descending number with zeros until it is 4 digits in length
# - subtract the ascending number from the descending number
# - repeat

# Problem: Given a number n, find the number of times this function needs to be applied to reach Kaprekar's Constant. 

import math

KAPREKAR_CONSTANT = 6174

def num_kaprekar_iterations(n):
	
	# split into a list
	n_string = str(n)
	n_list = []
	for num in n_string:
		n_list.append(num)

	# sort list ascending and descending
	n_asc = sorted(n_list)
	n_dsc = sorted(n_list, reverse=True) 
	# recombine both and convert to ints both
	j = '' #j is used an joining element
	n_asc_int = int(j.join(n_asc))
	n_dsc_int = int(j.join(n_dsc))
	
	#integers have no length property, use math to determine length
	if n_dsc_int > 0:
		n_length = int(math.log10(n_dsc_int))+1
	## ensure there are 4 digits in the final number
	if n_length == 4:
		n_dsc_int = n_dsc_int
	elif n_length < 2:
		n_dsc_int = n_dsc_int*1000
	elif n_length < 3:
		n_dsc_int = n_dsc_int*100
	else: 
		n_dsc_int = n_dsc_int*10
	# multiply by power of 10 until number is 4 digits in length
	
	# print(n_dsc_int)
	one_kap = (n_dsc_int - n_asc_int)
	# print(one_kap)

	n = one_kap
	# print(n, 'first kap')

	if n == 6174:
		return n
	else:
		return num_kaprekar_iterations(n)

	# return
 



print(num_kaprekar_iterations(123))


# 3
# Explanation:
# 3210 - 123 = 3087
# 8730 - 0378 = 8352
# 8532 - 2358 = 6174 (3 iterations)