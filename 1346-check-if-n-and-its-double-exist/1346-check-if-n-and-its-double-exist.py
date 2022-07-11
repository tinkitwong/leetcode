class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        """  Constraints
        i != j
        0 <= i, j < arr.length
        arr[i] == 2 * arr[j]
        """
        table = {}
        for num in arr:
            if num * 2 in table or num / 2 in table:
                return True
            if num not in table:
                table[num] = None
        return False
        
            