# encoding=utf-8
'''


    There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

    The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs0 is the cost of painting house 0 with color red; costs1 is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

    Note: All costs are positive integers.

'''

class Solution:
    def minCost(self, costs):
        pre = [0] * 3   # 当前为某种颜色,  三种颜色最小的总花费
        for x in costs:
            pre = [x[i] + min(pre[:i] + pre[i+1:]) for i in range(3)]   # prev[:i] + prev[i+1:] 产生了新的array
        return min(pre)

s = Solution()
print s.minCost([[1, 4, 2], [5, 2, 1]])