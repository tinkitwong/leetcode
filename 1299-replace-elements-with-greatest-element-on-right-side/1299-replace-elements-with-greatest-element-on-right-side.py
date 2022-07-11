class Solution:
    def replaceElements(self, arr: list) -> list:
        """
        Given an array arr, replace every element in that array with the greatest element among the elements to its right, 
        and replace the last element with -1.
        """
        # check edge cases
        if len(arr) == 0: return False
        if len(arr) == 1: return [-1]

        # iterate through input arr
        # get the max element among all elements to the right
        # replace current with that 

        for i in range(len(arr)):
            if i == len(arr)-1 : arr[i] = -1;break
            tmp = arr[i]
            # print(f"arr[i+1]: {arr[i+1:]}, arr: {arr}")
            ele_max = max(arr[i+1:])
            # index_max = arr.index(ele_max)
            arr[i] = ele_max
            # arr[index_max] = tmp


        return arr

# print(Solution().replaceElements([17,18,5,4,6,1]))