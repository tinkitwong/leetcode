class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # if item == 0; 
        # move all elements in next index onwards right once
        # then insert 0 in the next index and pop the last element
        isDuplicate = False
        for i in range(len(arr)-1):
            if isDuplicate: 
                isDuplicate = False
                continue
            if arr[i] == 0:
                arr = self.insert(arr, i)
                arr[i+1] = 0
                isDuplicate = True
                
                
                
        
    def insert(self, arr, index):
        for i in range(len(arr)-2,index,-1):
            arr[i+1] = arr[i]
        # print(f"this is the arr insert : {arr}")
        return arr