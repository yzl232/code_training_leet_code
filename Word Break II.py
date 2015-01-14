'''
 Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
'''


class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def check(self, s):
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for k in range(i):
                if dp[k] and s[k:i] in self.dict:    dp[i] = True
        return dp[-1]

    def dfs(self, s,  cur):
        if self.check(s):
            if not s:
                self.ret.append(cur[1:]) #[1:]  very clever!
                return
            for i in range(1, len(s) + 1):
                if s[:i] in self.dict:     self.dfs(s[i:],  cur+' ' + s[:i])

    def wordBreak(self, s, dict):
        self.ret = []; self.dict = dict
        self.dfs(s, '')
        return self.ret

# 可以用trie预处理