class Solution:
    def mySqrt(self, x: int) -> int:
        # create numbers from 0 ... x
        # check from 0 ...a-1, a... x, to see if a * a >= x st. a-1 * a-1 < x
        
        # cases:
        # i * i > x and i-1 * i-1 < x return i-1
        # i * i = x return i
        # i * i < x continue
        if x == 0: return 0
        for i in range(1,x+1):
            value = self.cases(i,x)
            if value:
                return value
        
        
        
        
    def cases(self, i:int, x:int) -> int or None:
        if (i*i > x and i-1 * i-1 < x):
            return i-1
        elif i*i == x:
            return i
        else:
            return
                