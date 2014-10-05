class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        n = len(prices)
        if len(prices) < 2: return 0
        profit = 0
        cur_min = prices[0]  #use this one to make sure the smallest one is before the most expensive one
        for i in range(len(prices)):
            profit = max(profit, prices[i] - cur_min)
            cur_min = min(cur_min, prices[i])
        return profit
        
        
        '''
        Say you have an array for which the ith element is the price of a given stock on day i.

        If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
        '''