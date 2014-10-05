class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        self.result = []; self.candidates = candidates
        self.dfs(0, target, [])
        return self.result
        
    def dfs(self, curNum, target, tmpResult):
        if target ==0:
            self.result.append(tmpResult)
            return
        elif target>0:
            for i in range(curNum, len(self.candidates)):
                c = self.candidates[i]
                if target>=c:
                    self.dfs(i, target-c, tmpResult+[c])