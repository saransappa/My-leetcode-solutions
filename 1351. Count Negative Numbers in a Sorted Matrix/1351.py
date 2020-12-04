class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in grid:
            count+=len([j for j in i if j<0])
        return count