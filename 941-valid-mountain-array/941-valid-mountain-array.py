class Solution:
    def validMountainArray(self, arr) -> bool:
        # check min. length
        if len(arr) < 3: return False

        index=0
        # check increasing until index i
        for i in range(len(arr)-1):
            print(f"i : {i}, index: {index}")
            if arr[i] < arr[i+1] :
                continue
            elif arr[i] == arr[i+1]:
                return False
            else:
                index=i
                break
        # rmb index i
        print(f"index: {index}")
        
        # check if arr is strictly decreasing
        if index == 0 : return False
        
        # check decreasing from index onwards
        for j in range(len(arr)-1, index, -1):
            print(f"arr[j]: {arr[j]} < arr[j-1]: {arr[j-1]}")
            if arr[j] < arr[j-1] and j != index+1:
                continue
            elif arr[j] == arr[j-1]:
                return False
            elif arr[j] < arr[index] and j == index+1:
                return True
            else:
                return False
        
        