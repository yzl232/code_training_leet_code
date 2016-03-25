class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, k, vals):
        k = min(k, len(vals)+1)
        sell=[0]*(k+1)   # hold 0 stocks
        buy=[-10**10]*(k+1)   #  hold 1 stocks
        for x in vals:
            for j in range(1, k+1):
                sell[j] = max(sell[j], buy[j]+x)  #最多j次交易卖掉了1张股票的最大值。
                buy[j] = max(buy[j], sell[j-1]-x)    #最多j次交易买了1张股票的最大值。
        return sell[-1]