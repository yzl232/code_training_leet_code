'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


'''

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, k, vals):
        if k >= len(vals) / 2:       return sum(max(0, vals[i]-vals[i-1]) for i in range(1, len(vals)))   # best time to buy stock II
        notHold=[0]*(k+1)   # hold 0 stocks
        hold = [float("-inf")]*(k+1)  #  hold 1 stocks
        for x in vals:
            for j in range(1, k+1):  #有链接先后的关系。
                notHold[j] = max(notHold[j], hold[j]+x)  #最多j次交易卖掉了1张股票的最大值。
                hold[j] = max(hold[j], notHold[j-1]-x)    #最多j次交易买了1张股票的最大值。
        return notHold[-1]