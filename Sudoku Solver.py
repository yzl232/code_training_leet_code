class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.

    def solveSudoku(self, board):
        board_List = []
        for row in board:
            board_List.append(list(row))
        self.dfs(board_List)
        for i in range(9):
            board[i] = ''.join(board_List[i])
        
    def dfs(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in range(9):
                        ch = chr(ord('1')+k)
                        board[i][j] = ch
                        if self.isValid(board, i, j):
                            if self.dfs(board):
                                return True
                        board[i][j] = '.'
                    return False     #1~9. All failed. Stop and it's False
        return True   # all filled. with no '.' exist
        
        
        
    def isValid(self, board, i, j):
        for k in range(9):
            if board[k][j] == board[i][j] and (k!=i): return False
            if board[i][k] == board[i][j] and (k!=j): return False
        
        r = i/3
        r = r * 3
        c = j/3
        c = c*3
        
        for m in range(3):
            for n in range(3):
                if (r+m == i) and (c+n == j): continue
                if board[r+m][c+n] == board[i][j]: return False
        
        return True
        
        