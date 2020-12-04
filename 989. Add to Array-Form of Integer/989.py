class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        for i in range(len(A)):
            A[i]=str(A[i])
        z = ''.join(A)
        A = int(z)+K
        return list(str(A))