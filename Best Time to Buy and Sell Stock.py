'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
'''

##和facebook的largest drop是一样的。

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, arr):  #和maxiMum subarray, product subaarray一模一样
        ret=0; minN = 10**10
        for x in arr:
            ret = max(ret, x-minN)
            minN = min(x, minN)
        return ret

'''
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, arr):  #和maxiMum subarray, product subaarray一模一样
        ret=0; maxN = -10**10
        for x in arr:
            ret = max(ret, x+maxN)
            maxN = max(-x, maxN)
        return ret
'''