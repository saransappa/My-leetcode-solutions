class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = ""
        for i in range(len(s)):
            for j in range(len(indices)):
                if indices[j]==i:
                    ans += s[j]
        return ans