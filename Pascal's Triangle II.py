'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,.
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?


'''
class Solution:
    # @return a list of integers
    def getRow(self, n):
        ret = [1]
        for i in range(n):
            ret = [1] + [ret[j]+ret[j+1] for j in range(len(ret)-1) ] + [1]
        return ret



'''
class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        result = [1]
        for i in range(rowIndex):
            preNum = 1
            for j in range(1, i+1):  #第一个1不用更新。从1开始
                preNum, result[j] = result[j], result[j]+preNum
            result+=[1]
        return result
'''

'''
class Solution:
    # @return a list of integers
    def getRow(self, numRows):
        result = [[1]]
        for i in range(numRows):
            oldRow = result[-1]
            newRow = []
            for j in range(len(oldRow)-1):
                newRow.append(oldRow[j]+oldRow[j+1])
            result.append([1]+newRow+[1])
        return result[-1]
'''