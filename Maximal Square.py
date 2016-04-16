'''
 Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 4. 
'''

class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix: return 0
        m, n, ret = len(matrix), len(matrix[0]), 0
        dp = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):  # 不是从(1, m), (1, n), 因为ret可能在第一列或第一行.
                if i and j and dp[i][j]:  dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                ret = max(ret, dp[i][j])
        return ret * ret