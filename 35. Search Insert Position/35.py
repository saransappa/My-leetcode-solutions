class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            for i in range(len(nums)):
                if nums[i]==target:
                    return i
        else:
            nums.append(target)
            nums.sort()
            for i in range(len(nums)):
                if nums[i]==target:
                    return i