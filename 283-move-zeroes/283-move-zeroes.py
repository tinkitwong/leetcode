class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
        """
        insert_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_index] = nums[i]
                insert_index += 1 
        
        for i in range(insert_index, len(nums)):
            nums[i] = 0
