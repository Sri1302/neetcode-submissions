class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1 # left= buy, right = sell
        maxP = 0
        # the only condition to keep in mind is r should be in range of prices
        while r <len(prices):
            #profitable?
            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
                maxP = max(maxP,profit)
            else:
                l= r
            r+=1
        return maxP