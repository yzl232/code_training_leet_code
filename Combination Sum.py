'''
 Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
    The solution set must not contain duplicate combinations.

For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]
'''

#permutation 一般是  t = c[:].  t.pop(i).   self.dfs
#combination 一般是  self.dfs(   , c[:])
#都是 for i in range(c)
# 题目说了，都是正数
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, arr, target):
        arr.sort();       self.ret = []; self.arr = arr
        self.dfs(0, target, [])
        return self.ret

    def dfs(self, st, target, cur):
        if target ==0:
            if cur not in self.ret: self.ret.append(cur)  #这样反而更合适。 考虑 combiantion sum II的关系。
            return
        for i in range(st, len(self.arr)):
            x = self.arr[i]
            if target>=x:              self.dfs(i, target-x, cur+[x])
# #if i>0 and self.c[i]==self.c[i-1]: continue   #反正可以无限重复使用。 跳过吧。