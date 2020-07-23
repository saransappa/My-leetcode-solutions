class Solution:
    def findComplement(self, num: int) -> int:
        z = bin(num)
        z = z[2:]
        z = z.replace('0','a')
        z = z.replace('1','b')
        z = z.replace('a','1')
        z = z.replace('b','0')
        return int(z,2)