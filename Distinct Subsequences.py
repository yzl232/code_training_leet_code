'''
 Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
'''
class Solution:
    # @return an integer    http://blog.csdn.net/abcbc/article/details/8978146
    #if S[i-1] == T[j-1]:  dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    # else:  dp[i][j] = dp[i-1][j]
    #  initial:  0 for all    .    dp[i][0] = 1    dp[0][i] = 0 (delete all)   dp[0][0] = 1   注意到当最后的字符串相等的时候，我们可以让S匹配T[-1]或者不匹配TT[-t]
    def numDistinct(self, s, t):
        m = len(s);  n = len(t)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]   #如果不用m+1, n+1 。  那么初始化， 会很麻烦
        for i in range(m+1):
            dp[i][0] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i-1] == t[j-1] else dp[i-1][j]
        return dp[-1][-1]

'''
class Solution4:
    # @return an integer    http://blog.csdn.net/abcbc/article/details/8978146
    #if S[i-1] == T[j-1]:  dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    # else:  dp[i][j] = dp[i-1][j]
    #  initial:  0 for all    .    dp[i][0] = 1    dp[0][i] = 0 (delete all)   dp[0][0] = 1
    def numDistinct(self, s, t):
        if not t: return 1
        if not s: return 0
        ret = self.numDistinct(s[1:], t)
        if s[0]==t[0]: ret+= self.numDistinct(s[1:], t[1:])
        return ret
'''