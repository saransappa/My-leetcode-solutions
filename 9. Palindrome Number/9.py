class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x);
        t=s[::-1]
        if s==t:
            return True
        else:
            return False