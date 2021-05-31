class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        else:
            nums.sort()
            max_dif = -1
            for i in range(1,len(nums)):
                max_dif = max(max_dif, nums[i]-nums[i-1])
            return max_dif