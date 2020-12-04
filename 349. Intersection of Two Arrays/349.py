class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        k = set(nums1)
        l = set(nums2)
        return list(k.intersection(l))