class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        z = []
        l = 0
        m = n
        while m<2*n and l<n:
            z.append(nums[l])
            z.append(nums[m])
            l+=1
            m+=1
        return z