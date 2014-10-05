class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        self.result = []; self.n = n
        self.dfs(  0, 0, '')
        return self.result
        
    def dfs(self, leftN, rightN, tmpResult):
        if leftN==rightN == self.n: 
            self.result.append(tmpResult)
            return 
        if leftN <self.n:
            self.dfs(leftN+1, rightN, tmpResult+'(')
        if rightN <leftN <=self.n:
            self.dfs(leftN, rightN+1, tmpResult + ')') 