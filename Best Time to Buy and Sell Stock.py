'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
'''

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):  #和maxiMum subarray, product subaarray一模一样
        if len(prices)<2: return 0
        profit = 0;  curMin = prices[0]
        for i in range(1, len(prices)):
            curMin = min(curMin, prices[i])
            profit = max(prices[i]-curMin, profit)
        return profit