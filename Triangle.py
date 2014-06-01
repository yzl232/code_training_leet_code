class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        l = len(triangle)
        dp = [0 for i in range(l)]
        for row in triangle:
            oldDp = dp[:]
            for i in range(len(row)):
                if i==0:
                    dp[i] = oldDp[i]+ row[i]
                elif i == len(row)-1:
                    dp[i] = oldDp[i-1] + row[i]
                else:
                    dp[i] = min(oldDp[i-1], oldDp[i]) + row[i]
        return min(dp)
    #We use 2 arrays. dp for the current row, oldDp for the last row.    We scan each position in each row. 