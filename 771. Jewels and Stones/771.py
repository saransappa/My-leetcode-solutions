class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        sum = 0
        for i in J:
            sum+=S.count(i)
        return sum