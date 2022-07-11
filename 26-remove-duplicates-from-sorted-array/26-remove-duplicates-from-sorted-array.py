class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        keeper = 1
        for checker in range(1, len(nums)):
            if nums[checker] != nums[checker - 1]:
                nums[keeper] = nums[checker]
                keeper += 1
        return keeper