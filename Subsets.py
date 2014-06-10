class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, s):
        result = [[]]
        s.sort()
        for i in s:
            old = result[:]
            for j in old:
                result.append(j+[i])
        return result