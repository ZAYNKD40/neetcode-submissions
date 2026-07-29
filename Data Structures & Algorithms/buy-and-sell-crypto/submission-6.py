class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        maxpcurr = 0
        for r in range(1,len(prices)):
            if prices[r] < prices[l]:
                l = r
                continue
            elif prices[r] > prices[l]:
                maxpcurr = max(maxpcurr, prices[r] - prices[l])
        return maxpcurr