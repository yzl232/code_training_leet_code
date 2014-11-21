'''
 Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

'''


class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        self.k = k
        self.n = n
        self.result = []
        self.dfs(1, [], 0)
        return self.result

    def dfs(self, start, curList, count):
        if count == self.k:
            self.result.append(curList)
            return
        for i in range(start, self.n+1):
            self.dfs(i+1, curList+[i], count+1)  # i+1, but not start +1  .  which means only add the number that is bigger 