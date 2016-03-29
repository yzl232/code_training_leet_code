'''
 There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.
'''

class Solution:
    def minCostII(self, costs):
        return min(reduce(self.combine, costs)) if costs else 0

    def combine(self, tmp, house):
        m, n, i = min(tmp), len(tmp), tmp.index(min(tmp))
        tmp, tmp[i] = [m]*n, min(tmp[:i]+tmp[i+1:])
        return map(sum, zip(house, tmp))
