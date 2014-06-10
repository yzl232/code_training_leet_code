class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        num2Letter = {1:'', 2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        result = ['']
        for d in digits:
            letters = list(num2Letter[int(d)])
            result = [ x + y for x in result for y in letters]
        return  result