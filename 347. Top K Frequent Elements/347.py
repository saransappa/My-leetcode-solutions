class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        p = list(set(nums))
        l=[]
        for i in p:
            t = tuple()
            t = (nums.count(i),i)
            l.append(t)
        l.sort(reverse=True)
        m = []
        for i in range(k):
            m.append(l[i][1])
        return m