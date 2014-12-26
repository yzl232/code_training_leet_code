'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
'''
class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def invalid(self, arr):
        arr = [i for i in arr if i!='.']
        return len(set(arr)) != len(arr)
        
    def isValidSudoku(self, board):  #第i行。 第i列检查
        for i in range(9):
            if self.invalid([board[i][j] for j in range(9)]) or self.invalid([board[j][i] for j in range(9)]): return False
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                if self.invalid([board[x][y] for x in range(i, i+3) for y in range(j, j+3)]): return False
        return True