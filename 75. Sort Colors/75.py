class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = nums.count(0)
        l = nums.count(1)
        m = nums.count(2)
        for i in range(len(nums)):
            if k>0:
                nums[i] = 0
                k-=1
            elif l>0:
                nums[i] = 1
                l-=1
            elif m>0:
                nums[i] = 2
                m-=1