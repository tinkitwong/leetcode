class Solution:
    def isSpecialCase(self, currentLetter, s):
        if s.index(currentLetter) + 1 == len(s):
            return
        else:
            nextCharIndex  = s.index(currentLetter) + 1 
            
        if currentLetter == "I":
            if s[nextCharIndex] == "V":
                # 4 
                return 4
            elif s[nextCharIndex] == "X":
                # 9
                return 9
            else: return
        elif currentLetter == "X":
            if s[nextCharIndex] == "L":
                # 40 
                return 40
            elif s[nextCharIndex] == "C":
                # 90
                return 90
            else: return
        elif currentLetter == "C":
            if s[nextCharIndex] == "D":
                # 400 
                return 400
            elif s[nextCharIndex] == "M":
                # 900
                return 900
            else: return
        return 
    
    def romanToInt(self, s: str) -> int:
        # variables
        table = {
            "I": 1,
            "V": 5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        n = len(s)
        ERRCODE = -1

        # constraints
        if n not in range(1,16): return ERRCODE
        
        digit = 0
        i = 0
        # iterate s: 
        while i < n:
            
            if s[i] not in table.keys(): return ERRCODE
            tmp = self.isSpecialCase(s[i],s)
            if tmp is not None:
                digit += tmp
                i += 2
            else: # is None: just take the current Roman Letter
                digit += table[s[i]]
                i += 1

        return digit

s = "DCXXI"
print(Solution().romanToInt(s))