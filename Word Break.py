class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    # dp[i] = any of ( dp[j] and s[j+1:i] )  0<=j<i
    def wordBreak(self, s, dict):
        n = len(s)
        dp = [False for i in range(n+1)]
        dp[0] = True
        for i in range(1, n+1):
            for j in range(0, i):
                if dp[j] and (s[j:i] in dict):
                    dp[i] = True
                    break
        return dp[n]
        
    '''
     Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

    For example, given
    s = "leetcode",
    dict = ["leet", "code"].

    Return true because "leetcode" can be segmented as "leet code".
    
    '''