class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num))>1:
            k = str(num)
            sum = 0
            for i in k:
                sum+=int(i)
            num = sum
        return num