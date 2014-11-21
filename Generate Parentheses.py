'''
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
'''

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        self.result =[]
        self.dfs(n, n, '')
        return self.result

    def dfs(self, l, r, tmpResult):
        if l == r == 0:
            self.result.append(tmpResult)
            return
        if l>0:
            self.dfs(l-1, r, tmpResult+'(')
        if r>l:
            self.dfs(l, r-1, tmpResult+')')