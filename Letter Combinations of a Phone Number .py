'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
'''
# encoding=utf-8
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        d = {1:'', 2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        cur = [""]
        for ch in digits:
            cur = [x+y for x in cur for y in d[int(ch)] ]     #x, y相互独立的时候，可以这样子压缩的。 如果有前后逻辑关系，就不行。
        return cur
'''

class Solution:
    def letterCombinations(self, digits):
        self.d = {1:'', 2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        self.ret = []
        self.dfs("", digits)
        return self.ret

    def dfs(self,  cur, digits):
        if not digits:
            self.ret.append(cur)
            return
        for ch in self.d[int(digits[0])]:
            self.dfs(cur+ch, digits[1:])

'''