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
        return [a+b if c == '+' else (a-b if c == '-' else a*b)
                for i, c in enumerate(s) if c in '+-*'
                for a in self.diffWaysToCompute(s[:i])
                for b in self.diffWaysToCompute(s[i + 1:])] or [int(s)]
# 类似 [x+y+z for x in range(10) for y in range(10) for z in range(10)]
'''
class Solution(object):
    def diffWaysToCompute(self, s):
        ret = []
        for i, ch in enumerate(s):
            if ch in '+-*':
                for a in self.diffWaysToCompute(s[:i]):
                    for b in self.diffWaysToCompute(s[i+1:]):
                        ret.append(a+b if ch == '+' else (a-b if ch == '-' else a*b))
        return  ret or [int(s)]
'''