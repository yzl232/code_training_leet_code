class Solution:
    # @return a list of integers
    def getRow(self, numRows):
        result = []
        for i in range(numRows+1):
            result.append([1]*(i+1))
        for i in range(numRows+1):
            if i == 0: continue
            temp = [0] + result[i-1] + [0]
            for j in range(i+1):
                result[i][j] = temp[j] + temp[j+1]
        return  result[-1]
        
        
        '''
        Given an index k, return the kth row of the Pascal's triangle.

        For example, given k = 3,
        Return [1,3,3,1].

        Note:
        Could you optimize your algorithm to use only O(k) extra space?

        
        '''