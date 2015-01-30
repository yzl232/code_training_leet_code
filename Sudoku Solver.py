'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
'''
class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.

    def solveSudoku(self, board):
        board_List = [list(i) for i in board ]
        self.dfs(board_List)
        for i in range(9):  board[i] = ''.join(board_List[i])

    def dfs(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for ch in '123456789':
                        board[i][j] = ch
                        if self.isValid(board, i, j) and self.dfs(board):     return True
                        board[i][j] = '.'
                    return False     #1~9. All failed. Stop and it's False
        return True   # all filled. with no '.' exist

    def isValid(self, board, i, j):
        for k in range(9):
            if board[k][j] == board[i][j] and (k!=i): return False   #valid sudoku全部检查。  这个只是添加了一个元素。 
            if board[i][k] == board[i][j] and (k!=j): return False  #不需要完全检查
        r=i-i%3; c=j-j%3
        for m in range(r, r+3):
            for n in range(c, c+3):
                if (m == i) and (n == j): continue
                if board[m][n] == board[i][j]: return False
        return True