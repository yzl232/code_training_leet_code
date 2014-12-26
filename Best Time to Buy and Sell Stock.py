'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
'''
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, arr):  #和maxiMum subarray, product subaarray一模一样
        if not arr: return 0
        ret=0; minN = arr[0]
        for i in range(1, len(arr)):
            ret = max(ret, arr[i]-minN)
            minN = min(arr[i], minN)
        return ret
##和facebook的largest drop是一样的。