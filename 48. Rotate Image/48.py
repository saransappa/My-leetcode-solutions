class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ans = []
        for i in range(len(matrix[0])):
            k = []
            for j in  matrix:
                k.append(j[i])
            k = k[::-1]
            ans.append(k)
        for i in range(len(matrix)):
            matrix[i] = ans[i]