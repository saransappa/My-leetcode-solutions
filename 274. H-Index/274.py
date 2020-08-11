class Solution:
    
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for k in range(len(citations),-1,-1):
            c = 0
            for i in citations:
                if i>=k:
                    c+=1
            if c>=k:
                return k
                break
        return 0