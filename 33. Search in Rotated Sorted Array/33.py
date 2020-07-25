class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        else:
            for i in range(len(nums)):
                if nums[i]==target:
                    return i
                
