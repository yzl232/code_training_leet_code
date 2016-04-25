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
        self.n=n=len(s); self.ret = []; self.s=s
        self.dp=dp=[[False]*n for i in range(n)]   # #保证了当i>j时， 仍然是False
        for j in range(n):   #知道长度从小到大， 就明白了。
            for i in range(j, -1, -1):
                if s[i]==s[j] and (j-i<=1 or dp[i+1][j-1]):  dp[i][j]=True
        self.dfs(0, [] )
        return self.ret

    def dfs(self,  start ,cur):
        if start==self.n:
            self.ret.append(cur)
            return
        for end in range(start, self.n):
            if self.dp[start][end]: self.dfs(end+1, cur+[self.s[start:end+1]])