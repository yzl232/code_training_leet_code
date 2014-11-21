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
        self.s, self.res, self.lenS = s, [], len(s)
        self.isPal = [ [False for i in range(self.lenS)] for j in range(self.lenS) ]
        for j in range(self.lenS):
            for i  in range(j+1): #保证了当i>j时， 仍然是False 
                if s[i] == s[j] and (j-i<=1 or self.isPal[i+1][j-1] == True):  
                    self.isPal[i][j] = True
        self.dfs(0, [])
        return self.res

    def dfs(self, start, L):
        if start == self.lenS:
            self.res.append(L)
            return
        for end in range(start, self.lenS):
            if self.isPal[start][end] == True:
                self.dfs(end+1, L[:] + [self.s[start:end+1]])
