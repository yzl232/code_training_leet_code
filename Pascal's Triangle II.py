class Solution:
    # @return a list of integers
    def getRow(self, numRows):
        if numRows == 0 : return [1]
        results = []
        for i in range(numRows+1):
            results.append([1]*(i+1))
        
        
        for i in range(numRows+1):
            if i==0:
                continue
            temp = [0] + results[i-1] + [0]
            for j in range(i+1):
                results[i][j]=temp[j]+temp[j+1]
        return results[-1]
        