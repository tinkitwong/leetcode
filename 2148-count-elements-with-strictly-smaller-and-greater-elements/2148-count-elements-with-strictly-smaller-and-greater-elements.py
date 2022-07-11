class Solution:
    def countElements(self, nums: list) -> int:
        table = dict.fromkeys(nums, None)
        count = 0

        for num in nums:
            # print(f"{seen} | {any(num > val for val in seen.keys())} | {any(num < val for val in seen.keys())}")
            if any(num > val for val in table.keys()) and any(num < val for val in table.keys()):
                count += 1
        return count
                
            
            