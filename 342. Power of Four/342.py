class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num<=0:
            return False
        k = math.log(num,4)
        if k == int(k):
            return True
        else:
            return False