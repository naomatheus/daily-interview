""" Problem was recently asked by Facebook """

""" 
Given a matrix that is organized such that the numbers will always be sorted from left to right, and the first number of each row will always be greater than the last element of the last row - i.e.
(mat[i][0] > mat[i -1][-1]). 

Search for a specific value in the matrix and return whether it exists.
"""

matrix = [
	[1,3,5,8],
	[10,11,15,16],
	[24,27,30,31]
]


def searchMatrix(mat, value):


	# improve: 
	## abstract, rows as row_num. 
	#next row, if value is less than current row_num[i], value is not in next row_num[i+1]. Can return False

	for row_num, row in enumerate(mat):
		last_num_in_row = mat[row_num][len(row)-1]
		print(last_num_in_row)

		if value == last_num_in_row:
			return True

		if value < last_num_in_row:
			
			next 
			next_row = mat[row_num+1]
			row = next_row
			
			return False, 'first false'
		# get to last val of each row
		elif value > last_num_in_row:
			next
			for idx, num in enumerate(row):
				if value == num:
					return True

	# if value is greater than last_num_in_row, then search next row row_num[i+1], 
	# next row is now current row_num[i]


	## access each row of the matrix

		for idx,num in enumerate(row):
			# while iterating each indv row of the matrix, check for equality with value
			if value == num:
				return True

			else:
				next
				
			# if value not present in any row, return False

	return False			

print(searchMatrix(matrix,4))
# # False
print(searchMatrix(matrix,10))
# # True