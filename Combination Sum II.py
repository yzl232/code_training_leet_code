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
    def combinationSum2(self, candidates, target):
        self.result = []
        candidates.sort()
        self.candidates = candidates
        self.dfs(0, target, [])
        return self.result
        
    def dfs(self, curNum, target, tmpResult):
        if target == 0: 
            if tmpResult not in self.result:
                self.result.append(tmpResult)
                return
        elif target>0:
            for i in range(curNum, len(self.candidates)):
                c = self.candidates[i] 
                if target >= c:
                    self.dfs(i+1, target-c, tmpResult+[c])#与前面的区别