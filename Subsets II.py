class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, s):
        s.sort()
        result = [[]]
        preSet = []
        for i in range(len(s)):
            old = result[:] if i==0 or s[i]!= s[i-1] else preSet[:]
            preSet = []
            for j in old:
                result.append(j+[s[i]])
                preSet.append(j+[s[i]])
        return  result