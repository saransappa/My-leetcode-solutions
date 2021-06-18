class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        left = 0
        right = 0
        k = 0
        for i in range(len(s)):
            if s[i]=='(':
                left+=1
            else:
                right+=1
            if left==right and left!=0:    
                ans += s[k+1:i]
                k =i+1
                left = 0
                right = 0
        return ans