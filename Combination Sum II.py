'''
 Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:

    All numbers (including target) will be positive integers.
    Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
    The solution set must not contain duplicate combinations.

For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
'''

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, c, target):
        c.sort();     self.ret = []; self.c = c
        self.dfs(0, target, [])
        return self.ret

    def dfs(self, n1, target, cur):
        if target ==0:
            if cur in self.ret: return
            self.ret.append(cur)
            return
        for i in range(n1, len(self.c)):
            x = self.c[i]   #不能跳过的  if i>0 and self.c[i]==self.c[i-1]: continue
            if target>=x:   self.dfs(i+1, target-x, cur+[x])