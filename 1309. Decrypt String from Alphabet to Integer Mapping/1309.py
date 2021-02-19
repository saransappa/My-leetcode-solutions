class Solution:
    def freqAlphabets(self, s: str) -> str:
        alpha = 'abcdefghijklmnopqrstuvwxyz'[::-1]
        for i in alpha:
            k = ord(i)-ord('a') + 1
            if k>9:
                p = str(k)+'#'
                s = s.replace(p,i)
            else:
                p = str(k)
                s = s.replace(p,i)
        return s