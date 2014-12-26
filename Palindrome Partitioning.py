'''
 Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]

'''

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        self.s, self.ret, self.n = s, [], len(s)
        self.dp = [ [False for i in range(self.n)] for j in range(self.n) ]
        for j in range(self.n):
            for i  in range(j+1): #保证了当i>j时， 仍然是False
                if s[i] == s[j] and (j-i<=1 or self.dp[i+1][j-1] == True):     self.dp[i][j] = True
        self.dfs(0, [])
        return self.ret

    def dfs(self, start, cur):
        if start == self.n:
            self.ret.append(cur)
            return
        for end in range(start, self.n):
            if self.dp[start][end] == True:  self.dfs(end+1, cur+ [self.s[start:end+1]])

