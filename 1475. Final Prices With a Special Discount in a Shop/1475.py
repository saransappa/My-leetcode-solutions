class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        l = []
        for i in range(len(prices)):
            found = False
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    l.append(prices[i]-prices[j])
                    found = True
                    break
            if not found:
                l.append(prices[i])
        return l