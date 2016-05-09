'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,.
Return

[
 [1],
[1,1],
[1,2,1],
[1,3,3,1],
[1,4,6,4,1]
]


'''
class Solution:
    # @return a list of lists of integers
    def generate(self, n):
        if n<1: return []
        ret = [[1]]
        for i in range(n-1):
            ret.append([1]+[ret[-1][j]+ret[-1][j+1] for j in range(len(ret[-1])-1)]+[1])
        return ret