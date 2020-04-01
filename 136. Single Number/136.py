class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        list = []
        for i in nums:
            if i not in list:
                list.append(i)
            else:
                list.remove(i)
        return list[0]
            