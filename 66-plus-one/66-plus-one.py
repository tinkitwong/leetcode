class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # MSB ... LSB
        # digits does not contain leading 0s
        
        # combine the digits to int && ++
        value = int(''.join([str(digit) for digit in digits]))
        
        # return int list
        return list(str(value+1))
        
        