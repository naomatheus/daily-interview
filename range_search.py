## problem asked by twitter ##
# Given a sorted list of duplicates, and a target number n, find the range in which the number exists (represented as a tuple (low,high)), both inclusive.

# If the number does not exist in the list, return (-1,-1)

case = [1,1,3,5,7]
tar = 1
case2 = [1,2,3,4]
tar2 = 5

def find_num(nums,target):
	high = 0
	low = 0
	# enumerate the array to find (x,y) of range
	for enum,n in enumerate(nums):
		if target not in nums:
			return (-1,-1)
		# base, if target not in array, return (-1,-1)

		if n == target:
			low = enum
			if low == 1:
				low-=1
		""" if pass of base, 
		the index enum containing the target element minus one is the low end of inclusive range """

		if n != target:
			high = enum - 1
			break
				
	""" the index containing the target element plus one is the high end of inclusive range """

	return (low,high)

print(find_num(case,tar))
print(find_num(case2,tar2))

## EXAMPLES WITH EXPECTED OUTPUT
# print(find_num([1,1,3,5,7],1))
# (0,1)

# print(find_num([1,2,3,4],5))
# (-1,-1)