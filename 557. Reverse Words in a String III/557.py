class Solution:
    def reverseWords(self, s: str) -> str:
        k = s.split()
        for i in range(len(k)):
            k[i]=k[i][::-1]
        return ' '.join(k)