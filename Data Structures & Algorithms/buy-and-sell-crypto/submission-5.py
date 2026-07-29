class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        maxp = 0
        for r in range(1,len(prices)):
            if prices[r] < prices[l]:
                l = r
                continue
            elif prices[r] > prices[l]:
                maxpcurr = max(0, prices[r] - prices[l])
                maxp = max(maxp, maxpcurr)
        return maxp