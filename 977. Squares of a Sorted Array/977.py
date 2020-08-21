class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        k = [i**2 for i in A]
        return sorted(k)