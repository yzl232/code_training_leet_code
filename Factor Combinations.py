'''
题目：

Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.

Write a function that takes an integer n and return all possible combinations of its factors.

Note:

    Each combination's factors must be sorted ascending, for example: The factors of 2 and 6 is [2, 6], not [6, 2].
    You may assume that n is always positive.
    Factors should be greater than 1 and less than n.
    
    
Examples:
input: 1
output:

[]

input: 37
output:

[]

input: 12
output:

[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]

input: 32
output:

[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]

'''

class Solution:
    def getFactors(self, n):
        self.rets = []
        def dfs(n, st, cur):
            for i in range(st, int(n**0.5)+1):
                if n % i == 0:
                    self.rets.append(cur + [i, n / i])  #因为下一层dfs里边, 也是到n**0.5为止不会考虑i本身的.
                    dfs(n / i, i, cur + [i])
        dfs(n, 2, [])
        return self.rets

'''
class Solution:
    def getFactors(self, n):
        self.rets = []
        self.dfs(2, [], n)
        return self.rets

    def dfs(self, start, cur, n):
        if n<1: return 
        if n==1:
            if len(cur)>1: self.rets.append(cur)
            return 
        for i in range(start, n+1):
            if n%i==0:   self.dfs(start, cur+[i], n/i)


class Solution:
    def getFactors(self, n):
        def factor(n, i, combi, combis):
            while i * i <= n:
                if n % i == 0:
                    combis += combi + [i, n/i],
                    factor(n/i, i, combi+[i], combis)
                i += 1
            return combis
        return factor(n, 2, [], [])
'''
