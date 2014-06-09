class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        self.result = []
        self.dfs(candidates, target, [])
        return self.result

    def dfs(self, candidates, target, tmpResult):
        if target == 0:
            self.result.append(tmpResult)
            return
        for i in range(len(candidates)):
            if target-candidates[i]>=0:
                self.dfs(candidates[i:], target-candidates[i], tmpResult+[candidates[i]])
