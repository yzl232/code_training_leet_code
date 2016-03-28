'''
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1

Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2

Output: [0, 2]

Example 2

Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

Output: [-34, -14, -10, -10, 10]

'''

class Solution(object):
    def diffWaysToCompute(self, s):
        self.cache = {}
        return self.dfs(s)

    def dfs(self, s):
        if s in self.cache: return self.cache[s]
        ret = []
        for i, ch in enumerate(s):
            if ch in '+-*':
                for a in self.dfs(s[:i]):
                    for b in self.dfs(s[i+1:]):
                        ret.append(a+b if ch == '+' else (a-b if ch == '-' else a*b))
        self.cache[s] = ret or [int(s)]
        return self.cache[s]
'''
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        return [a+b if c == '+' else a-b if c == '-' else a*b
            for i, c in enumerate(input) if c in '+-*'
            for a in self.diffWaysToCompute(input[:i])
            for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]
'''