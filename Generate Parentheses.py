'''
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
'''

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        self.ret =[]
        self.dfs(n, n, '')
        return self.ret

    def dfs(self, l, r, cur):
        if l == r == 0:
            self.ret.append(cur)
            return
        if l>0:    self.dfs(l-1, r, cur+'(')
        if r>l:    self.dfs(l, r-1, cur+')')