class Solution:
    def heightChecker(self, heights: list) -> int:
        """
        You are given an integer array heights representing the current order that the students are standing in. 
        Each heights[i] is the height of the ith student in line (0-indexed).

        Return the number of indices where heights[i] != expected[i].

        Constraints
        1 <= heights.length <= 100
        1 <= heights[i] <= 100
        """
        size = len(heights)
        expected = copy.deepcopy(heights)
        expected.sort()
        count = 0 
        if size > 100 or size < 1 : return None
        for i in range(size):
            if heights[i] > 100 or heights[i] < 1: return None

            if heights[i] != expected[i]: count +=1
        return count