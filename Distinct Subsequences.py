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
        lenS = len(s)
        lenT = len(t)
        dp = [[0 for j in range(lenT+1)] for i in range(lenS+1)]
        for i in range(lenS+1):
            dp[i][0] = 1
        for i in range(1, lenS+1):
            for j in range(1, lenT+1):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i-1] == t[j-1] else dp[i-1][j]
        return dp[-1][-1]

'''
class Solution:
    # @return an integer    http://blog.csdn.net/abcbc/article/details/8978146
    #if S[i-1] == T[j-1]:  dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    # else:  dp[i][j] = dp[i-1][j]
    #  initial:  0 for all    .    dp[i][0] = 1    dp[0][i] = 0 (delete all)   dp[0][0] = 1
    def numDistinct(self, s, t):
        if t=='': return 1
        elif s=='': return 0
        temp = self.numDistinct(s[:-1], t)
        if s[-1] == t[-1]:
            return self.numDistinct(s[:-1], t[:-1]) + temp
        else:
            return temp


'''