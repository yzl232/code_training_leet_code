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
                    self.dfs(i+1, target-c, tmpResult+[c])