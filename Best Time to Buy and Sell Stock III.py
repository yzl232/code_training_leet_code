'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

'''




class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, arr):
        b1 = b2 = -10**10  # 四个标记你的资产的量
        s1=s2=0  #不买亏的。max(0, xxx)
        for x in arr:
            s2 = max(s2, b2+x)   #反向来求。
            b2 = max(b2, s1-x)
            s1 = max(s1, b1+x)   #s1一定
            b1 = max(b1, 0-x)  # b1一定是个负数
        return s2

'''
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, arr):
        n=len(arr)
        if not arr: return 0
        l=[0 for i in range(n)]
        r=l[:]
        minN=arr[0]
        for i in range(1,n):
            minN=min(minN,arr[i])
            l[i]=max(l[i-1],arr[i]-minN)
        maxN=arr[-1]
        for i in range(n-2, -1, -1):
            maxN=max(maxN,arr[i])
            r[i]=max(r[i+1],maxN-arr[i])
        return max(l[i]+r[i] for i in range(n))
'''