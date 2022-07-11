"""
Need a way to rmb the previous maxCount
memory = [maxCount, maxCount_updated]
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0;
        maxCount_updated = 0;
        memory = {"maxCount": maxCount, "maxCount_updated": maxCount_updated}
        count = 0;
        for i in range(len(nums)):
            if i == 0 and nums[i] == 1:
                count+=1 
            elif i != 0 and nums[i] == 1 and nums[i-1] == 1:
                count+=1
            elif i !=0 and nums[i] == 1 and nums[i-1] == 0:
                count+=1 
            else:
                # check if memory.maxCount == 0 
                if memory["maxCount"] == 0:
                # if memory.maxCount == 0; then update it. 
                     memory["maxCount"] = count
                # if memory.maxCount_updated == 0; then update it. 
                elif memory["maxCount_updated"] == 0:
                    memory["maxCount_updated"] = count
                # else: take the max of memory.maxCount && memory.maCount_updated and the new count if there is 
                # assign max value to memory.maxCount and reset memory.maxCount_updated to 0
                else:
                    print(f"index: {i} ; number : {nums[i]} ; count: {count} ; dict : {memory}")
                    memory["maxCount"] = max(memory["maxCount"],memory["maxCount_updated"],count)
                    memory["maxCount_updated"] = 0
                count = 0
                
        memory["maxCount"] = max(memory["maxCount"],memory["maxCount_updated"])
        if memory["maxCount"] < count :
            memory["maxCount"] = count 
        return memory["maxCount"] 