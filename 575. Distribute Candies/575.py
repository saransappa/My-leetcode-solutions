class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        k = set(candyType)
        if len(k)<len(candyType)//2:
            return len(k)
        else:
            return len(candyType)//2