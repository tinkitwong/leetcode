class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        """
        Given an array of integers nums and an integer target, 
        return indices of the two numbers such that they add up to target.
        """
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - value
            if remaining not in seen:
                seen[value] = i
            else:
                return [i, seen[remaining]]

print(Solution().twoSum([3,2,4], 6))
        