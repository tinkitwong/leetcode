class Solution:
    def sortArrayByParity(self, nums: list) -> list:
        """
        Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
        """

        size = len(nums)
        """ constraints
        1 <= nums.length <= 5000
        0 <= nums[i] <= 5000
        """
        if size > 5000 or size < 1: return None
        if size == 1: return nums
        
        oddPointer = 0
        for i in range(size):
            if nums[i] > 5000 or nums[i] < 0: return None
            if nums[i] % 2 == 0:
                # do sth w even integers 
                tmp = nums[oddPointer]
                nums[oddPointer] = nums[i]
                nums[i] = tmp
                oddPointer += 1
            
        return nums