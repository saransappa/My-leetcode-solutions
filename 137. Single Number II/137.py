class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k = set(nums)
        for i in k:
            if nums.count(i)==1:
                return i