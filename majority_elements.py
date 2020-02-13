## question asked by AirBnB

# a majority element is an element that appears more than half time. Given a list with a majority element, find the majority element. 

test_list = [3,5,3,3,2,4,3]
test_list2 = [4,5,6,2,2,2,4,5]
test_list3 = [1,2,3,4,5]

def majority_element(nums):
	 
	# if the value at an index appears more times than the denom, return that value

	# count the num of occurences of each element
	count = {} # {k,v}
	## for each common key occurs 
	### increment the v of that key

	for num in nums:

		if num not in count:
			
			count[num] = 1
			
		else: 
			# num in count + 1
			count[num] += 1	
		
		# find the key that has max(count.values)
	for k,v in count.items():

		if v == max(count.values()):
			next
		if v.all() == v.all()
			return k
		
	return max(count.values())

print(majority_element(test_list))
print(majority_element(test_list2))
print(majority_element(test_list3))