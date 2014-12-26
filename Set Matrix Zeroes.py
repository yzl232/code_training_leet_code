#Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if not matrix:return
        m=len(matrix); n=len(matrix[0])
        first_0_row,first_0_col=False,False
        for i in range(m):      #利用第一行，第一列做辅助array
            if matrix[i][0]==0:  first_0_col=True
        for j in range(n):
            if matrix[0][j]==0: first_0_row=True
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:     matrix[0][j],  matrix[i][0]=0, 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:   matrix[i][j] = 0
        if first_0_row:    #第一行，第一列
            for i in range(n):  matrix[0][i]=0
        if first_0_col:
            for j in range(m):   matrix[j][0]=0
'''
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
'''