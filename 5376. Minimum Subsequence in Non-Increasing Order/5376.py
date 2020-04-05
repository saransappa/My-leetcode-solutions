class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        sum= 0
        if len(nums)<2:
            return nums
        for i in nums:
            sum+=i
        nums.sort()
        list = []
        k = 0
        for i in range(len(nums)-1,-1,-1):
            if k>sum-k:
                break
            k += nums[i]
            list.append(nums[i])
        return list