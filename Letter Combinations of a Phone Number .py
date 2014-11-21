'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
'''
# encoding=utf-8
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        numberToletter = {1:'', 2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        cur = [""]
        for d in digits:
            cur = [x+y for x in cur for y in numberToletter[int(d)] ]
        return cur
'''
class Solution:
    def letterCombinations(self, digits):
        self.numberToletter = {1:'', 2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        self.result = []
        self.dfs("", digits)
        return self.result

    def dfs(self,  tmpPath, digits):
        if not digits:
            self.result.append(tmpPath)
            return
        for ch in self.numberToletter[int(digits[0])]:
            self.dfs(tmpPath+ch, digits[1:])
'''