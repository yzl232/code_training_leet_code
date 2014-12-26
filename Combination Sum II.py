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
        c.sort()
        self.ret = [];
        self.dfs(target, [], c)
        return self.ret

    def dfs(self, target, cur,cans):
        if target<0: return
        if target ==0:
            self.ret.append(cur)
            return
        for i in range(len(cans)):
            x = cans[i]
            self.dfs(target-x, cur+[x], cans[i+1:]) #不可以重复使用, i:  不是i+1