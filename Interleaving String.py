class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        n1=len(s1); n2 =len(s2); n3 =len(s3)
        if n1 + n2 != n3:
            return False
        dp = [ [ False for i in range(n2+1)] for j in range(n1+1) ]
        dp[0][0] = True
        for i in range(1, n1+1):
            if s3[i-1] == s1[i-1]:
                dp[i][0] = True
            else: break

        for i in range(1, n2+1):
            if s3[i-1] == s2[i-1]:
                dp[0][i] = True
            else:
                break

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if dp[i-1][j] and s3[i+j-1] == s1[i-1]:
                    dp[i][j] = True
                if dp[i][j-1] and s3[i+j-1] == s2[j-1]:
                    dp[i][j] = True

        return dp[n1][n2]
