class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        p = [] 
        for i in digits:
            p.append(str(i))
        s = int(''.join(p))
        s+=1
        return list(str(s))
        