class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        result = []
        for i in range(numRows):
            result.append([1]*(i+1))
        for i in range(numRows):
            if i==0: continue
            temp =[0]+ result[i-1] + [0]
            for j in range(i+1):
                result[i][j] = temp[j] + temp[j+1]
        return result               