class Solution:
    def maxPower(self, s: str) -> int:
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        for k in range(len(s),-1,-1):
            for i in alpha:
                p = i*k
                if p in s:
                    return k