# encoding=utf-8
'''
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.
'''

class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, mtx):
        m=len(mtx); n=len(mtx[0])
        dp= [[10**10]*(n+1) for i in range(m+1)]
        dp[m][n-1]=1   #先写 dp[m-1][n-1]=dp[m-1][n-1]=1 . 然后改正加1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1])  - mtx[i][j],   1)  # if dp[i][j]<1: dp[i][j]=1
        return dp[0][0]
# 如果把dp的值存到dungeon matrix。 可以做到O(1) extra space
# http://leetcodesolution.blogspot.com/2015/01/leetcode-dungeon-game.html
# initial health 的解释
'''
class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, mtx):
        m=len(mtx); n=len(mtx[0])
        dp= [[0 for j in range(n)] for i in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i==m-1 and j==n-1: dp[i][j]=max(1, 1-mtx[m-1][n-1])
                elif i==m-1:  dp[i][j] = max(dp[i][j+1]-mtx[i][j], 1)
                elif j==n-1: dp[i][j] = max(dp[i+1][j]-mtx[i][j], 1)
                else:dp[i][j] =max( min(dp[i+1][j], dp[i][j+1])  - mtx[i][j],    1)
        return dp[0][0]
'''
# 为求得答案应该默认到终点时剩余的health是1.但是正推的话状态转移函数是什么呢，初始状态是什么呢，都没法回答. 所以必须倒推