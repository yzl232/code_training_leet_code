'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

'''

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        length = len(prices)
        if length<=0:
            return 0

        maxProfitForward = [0 for i in range(length)]
        minPrice = prices[0]
        maxProfit = -1

        for i in range(length):
            curPrice = prices[i]
            minPrice = min(minPrice, curPrice)
            maxProfit = max(curPrice - minPrice, maxProfit)
            maxProfitForward[i] = maxProfit

        maxProfitBackward = [0 for i in range(length)]
        maxPrice = prices[-1]
        maxProfit = -1

        for i in range(length-1, -1, -1):
            curPrice = prices[i]
            maxPrice = max(maxPrice, curPrice)
            maxProfit = max(maxPrice - curPrice, maxProfit)
            maxProfitBackward[i] = maxProfit

        result = maxProfitForward[-1] # Note this line
        for i in range(length-1):
            result = max(result, maxProfitForward[i] + maxProfitBackward[i+1])
        return result

'''
少一个pass
'''
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        n = len(prices)
        if n<=0: return 0
        profitForward = [0 for i in range(n)]
        minPrice = prices[0]
        maxProfit = 0

        for i in range(n):
            curPrice = prices[i]
            minPrice = min(minPrice, curPrice)
            maxProfit = max(maxProfit, curPrice - minPrice)
            profitForward[i] = maxProfit

        profitBackWard = [0 for i in range(n)]
        maxPrice = prices[-1]
        maxProfit = 0
        for i in range(n-1, -1, -1):
            curPrice = prices[i]
            maxPrice = max(maxPrice, curPrice)
            maxProfit = max(maxProfit, maxPrice-curPrice)
            profitBackWard[i] = maxProfit

        return max(profitForward[i]+profitBackWard[i] for i in range(n))