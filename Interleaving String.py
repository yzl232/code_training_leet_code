
'''
 Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

'''


class Solution:
    # @return a boolean
    d= {("", "", ""): True}
    def isInterleave(self, s1, s2, s3):
        if (s1, s2, s3) not in self.d:
            self.d[(s1, s2, s3)] = (s3!="" and s2!="" and s3[0]==s2[0] and self.isInterleave(s1, s2[1:], s3[1:])) or (s3!="" and s1!="" and s3[0]==s1[0] and self.isInterleave(s1[1:], s2, s3[1:]))
        return self.d[(s1, s2, s3)]


'''
class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        n1 = len(s1); n2 = len(s2); n3 = len(s3)
        if n1 + n2 != n3:   return False
        dp = [[False]*(n2 + 1) for j in range(n1 + 1)] ;   dp[0][0]=True
        for i in range(n1 + 1):   #1~n取决于空字串。 n+1
            for j in range(n2 + 1):
                if i > 0 and dp[i-1][j]  and s1[i-1] == s3[i+j-1]:   dp[i][j] =True
                if j > 0 and dp[i][j-1]  and s2[j-1] == s3[i+j-1]:   dp[i][j] =True
        return dp[n1][n2]

class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        n1=len(s1); n2 =len(s2); n3 =len(s3)
        if n1+n2!=n3: return False
        dp = [ [False]*(n2+1) for j in range(n1+1) ]  #这一句注意n+1， 以及n1的维度在外面
        dp[0][0] = True
        for i in range(1, n1+1):
            if s3[i-1] == s1[i-1]:    dp[i][0] = True
            else: break
        for j in range(1, n2+1):
            if s3[j-1] == s2[j-1]:   dp[0][j] = True
            else: break
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if dp[i][j-1] and s3[i+j-1] == s2[j-1]:   dp[i][j] = True
                if dp[i-1][j] and s3[i+j-1] == s1[i-1]:   dp[i][j] = True
        return dp[n1][n2]
# 可以先提一下，说recursion肯定可以做。  Basically   s3[i+j-1] == s2[j-1]  and self.isInterleave(s1, s2[:-1], s3[:-1]     或者    s3[i+j-1] == s1[j-1]  and self.isInterleave(s1[:-1], s2, s3[:-1]  )
# But I prefer using dynamic programming.

class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if s1 == '' and s2 == '' and s3 == '': return True
        if   len(s3)>0 and len(s2) >0 and s3[0] == s2[0]  and self.isInterleave(s1, s2[1:], s3[1:]): return True
        if   len(s3)>0 and len(s1) >0 and s3[0] == s1[0]   and self.isInterleave(s1[1:], s2, s3[1:]  ): return True
        return False

class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if not s1 and not s2 and not s3: return True
        if s3 and s2 and s3[0]==s2[0] and self.isInterleave(s1, s2[1:], s3[1:]): return True
        if s3 and s1 and s3[0]==s1[0] and self.isInterleave(s1[1:], s2, s3[1:]): return True
        return False

字符串的True or False, 天生比较适合DP。
因为都是char[i] == 'x' an dp[i-1]

一般来说，独立变量的个数决定动态规划的维度，例如l1和l2独立变化，所以用了二维动态规划

字符串的DP。 因为考虑空字符串。 所以都是 length+1



'''

