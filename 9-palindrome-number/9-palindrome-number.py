class Solution:
    def isPalindrome(self, x: int) -> bool:
        # solves without converting to a string
        if x < 0:
            return False
        num = x
        reverse = 0
        while(num):
            
            reverse = reverse * 10 + num % 10  #taking the reverse of the number
            print(num, reverse)
            num //= 10 # strip the last digit
            # print(num, x)
        return x == reverse
