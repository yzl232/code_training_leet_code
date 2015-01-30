'''
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

'''

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    # dp[i] = any of ( dp[j] and s[j+1:i] )  0<=j<i
    def wordBreak(self, s, dict):
        n = len(s);   dp = [False] *(n+1)
        dp[0] = True
        for j in range(1, n+1):  #n+1。 因为有必要用到''空作为基准
            for i in range(0, j):
                if dp[i] and (s[i:j] in dict):  #边界会很烦。  取j=1,  i=0.   'a'  对的。不是s[i+1:j]
                    dp[j] = True
                    break
        return dp[n]
#还是喜欢memoization啊。
'''
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    # dp[i] = any of ( dp[j] and s[j+1:i] )  0<=j<i
    def wordBreak(self, s, dict):
        if s=='': return True
        n = len(s)
        for i in range(0, n):
            if self.wordBreak(s[:i], dict) and s[i:] in dict:
                return True
        return False

'''

