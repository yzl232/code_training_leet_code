
'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''


class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):   #dp存到原来的grid。  in place
        m = len(grid);  n = len(grid[0])
        for i in range(1, m):  grid[i][0] += grid[i-1][0]
        for j in range(1, n):   grid[0][j] += grid[0][j-1]
        for i in range(1, n):
            for j in range(1, m):
                grid[j][i] += min(grid[j][i-1], grid[j-1][i])
        return grid[-1][-1]