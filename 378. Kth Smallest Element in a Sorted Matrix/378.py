class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        z = []
        for i in matrix:
            z.extend(i)
        z.sort()
        return z[k-1]