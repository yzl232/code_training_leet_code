class Solution:    # a little similar to Sudoku question
    # @return a list of lists of string   # since each line set once, we only need to check each column and each diagnoal
    def solveNQueens(self, n):
        self.result = []    # the one-dimension array stores the information where the queen locates
        self.solve(n, 0, [-1 for i in range(n)] )# because array is easier to manipulate
        return  self.result
    def solve(self, n, currQueenNum, board):
        if currQueenNum == n:  # recursion ends, prepare the answer
            oneAnswer = [['.' for j in range(n)] for i in range(n)]
            for i in range(n):
                oneAnswer[i][board[i]] = 'Q'
                oneAnswer[i] = ''.join(oneAnswer[i])
            self.result.append(oneAnswer)
            return
#Use a int vector to store the current state,  A[i]=j refers that the ith row and jth column is placed a queen
        for i in range(n):  # try every column
            valid = True
            for k in range(currQueenNum):  #  as I think, in range(n) is also fine  
                #chech column
                if board[k] == i:
                    valid = False
                    break
                if abs(board[k] - i) == abs(currQueenNum - k):
                    valid = False
                    break
            if valid:
                board[currQueenNum] = i
                self.solve(n, currQueenNum + 1, board)