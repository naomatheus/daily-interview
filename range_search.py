## problem asked by twitter ##
# Given a sorted list of duplicates, and a target number n, find the range in which the number exists (represented as a tuple (low,high)), both inclusive.

# If the number does not exist in the list, return (-1,-1)

case = [1,1,3,5,7]
tar = 1

def find_num(nums,target):


	high = 0
	low = 0
	## find and match target, find the first element in nums that matches target 
	for enum,n in enumerate(nums):
		print(enum,n)
		


		if n == tar:
			low = enum
			# print(low)
			if low == 1:
				low-=1
				# print(low)

		if n != tar:
			high = enum - 1
			break
			# if n != tar:
				# high = enum - 1



	#the index containing the target element minus one is the low end of inclusive range

	## the index containing the target element plus one is the high end of inclusive range

	return (low,high)

print(find_num(case,tar))

# print(find_num([1,1,3,5,7],1))
# (0,1)

# print(find_num([1,2,3,4],5))
# (-1,-1)