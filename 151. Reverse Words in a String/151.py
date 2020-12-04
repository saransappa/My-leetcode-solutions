class Solution:
    def reverseWords(self, s: str) -> str:
        k = s.split()
        k = k[::-1]
        return ' '.join(k)
