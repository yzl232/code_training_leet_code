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
        notHold, hold=[0]*(k+1), [float("-inf")]*(k+1)  # # hold 0 stocks,  hold 1 stocks
        for x in vals:  # 默认unhold[0], 买了一次hold[1], 卖了一次.unhold[1]
            for j in range(1, k+1):   #考虑不能同时买卖。 下面同时更新反而是很好的。
                notHold[j], hold[j] = max(notHold[j], hold[j]+x), max(hold[j], notHold[j-1]-x)    
        return notHold[-1]