'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

    You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
    After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]




'''

# https://leetcode.com/discuss/79283/4-line-python-solution-52-ms
class Solution(object):
    def maxProfit(self, prices):
        notHold, coolDown, hold = 0, 0, float('-inf')
        for x in prices:
            hold, notHold, coolDown = max(notHold-x, hold), max(coolDown, notHold), hold+x
'''
hold =>   cooldown,  hold
cooldown =>  unhold            cooldown由于冷却的存在, 不能直接买, 变成hold
unhold =>  unhold,  hold


'''


