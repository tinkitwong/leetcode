class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # len of digits : len(str(nums[i]))
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count 
        