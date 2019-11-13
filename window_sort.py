# Hi, here's your problem today.
#This # problem was recently asked by # Twitter:

# Given a list of numbers, find the
# smallest window to sort such that the
# whole list will be sorted. If the list is
# already sorted return (0, 0). You
# can assume there will be no duplicate
# numbers.

# Example:
# Input: [2, 4, 7, 5, 6, 8, 9]
# Output: (2, 4)

# Explanation: Sorting the window (2,
# 4) which is [7, 5, 6] will also
# means that the whole list is sorted.

def min_window_to_sort(nums):
	
	# establish a pointer position
	i = 0
	j = 0
	return_tuple = [0,0]
	pointer = 0

	
	#if the list is sorted return (0,0)
	if sorted(nums) == nums:
		return return_tuple
	# iterate through the lists values
	for i in range(len(nums)):
		## find the unsorted integer
		while nums[i] > nums[j+1]:
			# compare with (< or >) the first unsorted int with the next int
			pointer = i
			print(f'{i} is position of first unsorted int')
			return_tuple[0] = pointer
			
			i+=1
			j+=1
			# return return_tuple
			
			# if j is not sorted (less than the i), store the position of the unsorted int as position 0 in the tuple, 
			pointer+=1
			# then iterate the pointer
			while nums[j+1] > nums[i]:
				print('2nd while')
				if nums[j+1] > nums[i]:
					print('this if')
					print(nums[j-1])
					nums[j-1] = return_tuple[1]
					
					return return_tuple

		# if nums[i] < nums[j+1] or i >= len(nums):
		# 	# if the j is greater than i (sorted), iterate the pointer and continue until j is less than i 
		# 	i+=1
		# 	j+=1
		# 	pointer+=1
		# 	# print(nums[i])
		# 	return 
		# 	if i >= len(nums):
		# 		return 'list is sorted'




	# continue iterating the pointer, as the pointer continues, assign the position of the pointer to the 1 position in the tuple

	# if j is greater than the i, assign the i position to position 1 of the tuple, minus 1.

 
print(min_window_to_sort([2,4,7,5,6,8,9]))
	# (2, 4)