class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:
        """
        Given an array nums of n integers where nums[i] is in the range [1, n], 
        return an array of all the integers in the range [1, n] that do not appear in nums.

        Constraints
        n == nums.length
        1 <= n <= 105
        1 <= nums[i] <= n
        """
        print(set(range(1,len(nums)+1)))
        print(set(nums))
        return list(set(range(1,len(nums)+1))-set(nums))