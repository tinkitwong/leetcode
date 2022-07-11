class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unums, heap = set([]), []
        for x in nums:
            if x not in unums:
                heappush(heap, x)
                unums.add(x)
                if len(heap) == 4:
                    a = heappop(heap)
                    unums.remove(a)
        print(unums, heap)        
        if len(heap) == 2:
            x = heappop(heap)
        print(heap)
        return heap[0]