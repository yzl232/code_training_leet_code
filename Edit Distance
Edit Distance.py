class Solution:
    # @return an integer   # http://www.programcreek.com/2013/12/edit-distance-in-java/
    #dp[i, j] = min(dp[i-1, j-1], dp[i-1, j], dp[i, j-1]) + 1 if word1[i]!=word2[j] else dp[i-1, j-1]
    #dp[0, j] = j      dp[i, 0] = i      i, j means length
    def minDistance(self, word1, word2):
        dp = {}
        l1 = len(word1); l2 = len(word2)
        for i in range(l2+1):
            dp[0, i] = i
        for i in range(l1+1):
            dp[i, 0] = i
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                dp[i, j] = min(dp[i-1, j-1], dp[i-1, j], dp[i, j-1]) + 1 if word1[i-1]!=word2[j-1] else dp[i-1, j-1]
        return dp[l1, l2]