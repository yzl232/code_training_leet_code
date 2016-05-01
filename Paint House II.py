'''
 There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.
'''

class Solution:   
    def minCostII(self, costs):
        if not costs:  return 0
        cur = [0] * len(costs[0])
        for x in costs:
            cur = self.combine(cur, x)    #一直在对cur做处理.  也就是之前的被抛弃了.  
        return min(cur)

    def combine(self, one, two):  # N行, k种颜色.
        x = min(one);   i = one.index(x)  #  找到min后, 默认都选择min的那个颜色. 除了i以外.
        one, one[i]  = [x] * len(one), min(one[:i] + one[i + 1:] or [0]) # 考虑到先后因果关系。在同一行， 不然用tmp
        return [one[i]+two[i] for i in range(len(one))]
#the first time combine is called, tmp will be costs[0] and house will be costs[1]


'''
class Solution:
    def minCostII(self, costs):
        return min(reduce(self.combine, costs)) if costs else 0

    def combine(self, one, two):  # N行, k种颜色.
        x = min(one);   i = one.index(x)  #  找到min后, 默认都选择min的那个颜色. 除了i以外.
        one, one[i]  = [x] * len(one), min(one[:i] + one[i + 1:]) # 考虑到先后因果关系。在同一行， 不然用tmp
        return [one[i]+two[i] for i in range(len(one))]
#the first time combine is called, tmp will be costs[0] and house will be costs[1]
'''