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
	k = 0

	
	#if the list is sorted return (0,0)
	if sorted(nums) == nums:
		return return_tuple
	# iterate through the lists values
	for i in range(len(nums)):
		## find the unsorted integer
		while nums[i] > nums[j+1]:
			# compare with (< or >) the first unsorted int with the next int
			
			print(f'{i} is position of first unsorted int')
			return_tuple[0] = i
			
			i+=1
			j+=1
			
			# if j is not sorted (less than the i), store the position of the unsorted int as position 0 in the tuple, 
			k=j+1
			# then iterate the k
			while nums[j+1] > nums[k+1]:
				
				print(nums[j+1], 'numsj+1')
				k+=1
				print(nums[k],'numsk')
				
			if nums[k] > nums[j]:
				return_tuple[1] = k
					
				return return_tuple

		# if nums[i] < nums[j+1] or i >= len(nums):
		# 	# if the j is greater than i (sorted), iterate the k and continue until j is less than i 
		




	# continue iterating the k, as the k continues, assign the position of the k to the 1 position in the tuple

	# if j is greater than the i, assign the i position to position 1 of the tuple, minus 1.

 
print(min_window_to_sort([2,4,7,5,6,8,9]))
	# (2, 4)
print(min_window_to_sort([2,3,4,7,5,9,6,10]))