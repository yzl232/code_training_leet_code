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
class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid == [] : return 0
        m = len(obstacleGrid); n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1: break
            else: dp[i][0] = 1

        for i in range(n):
            if obstacleGrid[0][i] == 1: break
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1: continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]