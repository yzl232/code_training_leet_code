class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        self.s, self.res, self.l = s, [], len(s)
        self.isPal = [[False for i in range(self.l)] for j in range(self.l)]
        for j in range(self.l):
            for i in range(j, -1, -1):
                if s[i] == s[j] and (j - i<=1 or self.isPal[i+1][j-1]):
                    self.isPal[i][j] = True
        self.dfs(0, [])
        return self.res
        
    def dfs(self, start, L):
        if start == self.l:
            self.res.append(L)
        else:
            for end in range(start, self.l):
                if self.isPal[start][end]:
                    self.dfs(end+1, L[:] + [self.s[start:end+1]])

                                                                                                                                                                                                          