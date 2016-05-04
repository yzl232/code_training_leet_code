'''
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]

Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]

Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
'''


class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0]);  dp = [[None] * n for i in xrange(m)]
        def dfs(i, j):
            if dp[i][j]==None:    #set dp是不可以省略的
                dp[i][j] = 1 + max([dfs(x, y) for x,y in [(i-1, j),(i+1, j), (i, j-1), (i, j+1)] if (0<=x<m and 0<=y<n and matrix[i][j]>matrix[x][y])] or [0])
            return dp[i][j]
        return max(dfs(x, y) for x in xrange(m) for y in xrange(n))