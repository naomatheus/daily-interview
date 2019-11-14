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
	j = 0
	k = 0
	return_tuple = []
	#if the list is sorted return (0,0)
	if sorted(nums) == nums:
		return return_tuple
	
	for i in range(len(nums)):
		j = i + 1
		k = i
		print(k,'k')
		print(j,'j')
		if j >= len(nums):
			return 'end'



 
# print(min_window_to_sort([2,4,7,5,6,8,9]))
	# (2, 4)
print(min_window_to_sort([0,1,2,3,4,7,5,9,6,10]))
	# (4,8)