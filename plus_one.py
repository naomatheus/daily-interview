num = [2,9,9]

class Solution:
    def __init__(self,nums,limit):
        self.nums = nums
        self.limit = limit

    def plus_one(self):
        for n in range(len(self.nums)): 
        # Instead of iterating through each element you can can count up to the length of the list and modify the list directly
            if self.nums[n] == self.limit:
                self.nums[n] -= self.limit
            else:
                self.nums[n] += 1

        return self.nums


adder = Solution(num,9)

print('test',adder.plus_one())