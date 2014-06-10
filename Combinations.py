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