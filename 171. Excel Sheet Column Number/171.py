class Solution:
    def titleToNumber(self, s: str) -> int:
        s = s[::-1]
        col = 0
        for i in range(len(s)):
           col += (26**i)*(ord(s[i])-64)  
        return col