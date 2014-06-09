class Solution:
    # @return an integer    http://blog.csdn.net/abcbc/article/details/8978146
    #if S[i-1] == T[j-1]:  dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    # else:  dp[i][j] = dp[i-1][j]
    #  initial:  0 for all    .    dp[i][0] = 1    dp[0][i] = 0 (delete all)   dp[0][0] = 1
    def numDistinct(self, S, T):
        dp = {}
        for i in range(1, len(T)+1):
            dp[0, i] = 0
        for j in range(0, len(S)+1):
            dp[j, 0] = 1
        for i in range(1, len(S)+1):
            for j in range(1, len(T)+1):
                dp[i, j] = dp[i-1, j-1] + dp[i-1, j] if S[i-1] == T[j-1] else dp[i-1, j]
        return dp[len(S), len(T)]