'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,

There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

The total number of unique paths is 2.

Note: m and n will be at most 100.
'''

#存到原来的array可以做到O(1) space   (in place)
class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, grid):  #加上了dummy row, column to make it clean
        if not grid: return 0
        m=len(grid); n=len(grid[0])
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        dp[0][1]=1   #解决第一个dp[1][1] 的corner case
        for i in range(1, m+1):
            for j in range(1, n+1):
                if not grid[i-1][j-1]:  dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
