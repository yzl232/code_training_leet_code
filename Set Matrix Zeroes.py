class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if matrix == []:
            return
        row =set([])
        col = set([])
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in range(m):
            for j in range(n):
                if i in row or j in col:
                    matrix[i][j] = 0
        
        #Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place. 