
'''

 Given a collection of integers that might contain duplicates, S, return all possible subsets.

Note:

    Elements in a subset must be in non-descending order.
    The solution set must not contain duplicate subsets.

For example,
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

'''

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, s):
        ret = [[]];  s.sort()
        for x in s:
            ret +=[ y+[x] for y in ret if y+[x] not in ret]
        return ret
'''

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        self.result = []
        self.dfs([], S)
        return self.result

    def dfs(self, tmp, candidates):
        self.result.append(tmp)
        for i in range(len(candidates)):
            if i>0 and candidates[i] == candidates[i-1]: continue
            self.dfs(tmp+[candidates[i]], candidates[i+1:])
'''