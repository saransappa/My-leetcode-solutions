class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        k = list(set(nums))
        sum = 0
        for i in k:
            if nums.count(i)==1:
                sum+=i
        return sum