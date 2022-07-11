class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordList = list(filter(("").__ne__,s.split(" ")))
        return len(wordList[-1])
        