class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.

    def solveSudoku(self, board):
        board_list=[]
        for i in range(9):
            board_list.append(list(board[i]))
            #print board_list[i]


        self.dfs(board_list)
        for i in range(9):
            board[i] = ''.join(board_list[i])

    def dfs(self, board):

        for i in range(9):
            for j in range(9):
                if (board[i][j] == '.'):
                    for k in range(1, 10):
                        board[i][j] = chr(ord('0')+k)
                        if (self.isValid(board, i, j) and self.dfs(board)):
                            return True
                        board[i][j] = '.'
                    return False
        return True


    def isValid(self, board, i, j):
        for k in range(9):
            if board[i][k] == board[i][j] and k != j:
                return False
            if board[k][j] == board[i][j] and k != i:
                return False

        r = i/3
        c = j/3
        r = r*3
        c = c*3


        for k in range(3):
            for m in range(3):
                if board[r+k][c+m] == board[i][j] and ((r+k)!=i or (c+m)!=j):
                    return False

        return True

