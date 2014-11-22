'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
'''
class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(9):
            a = []
            for j in range(9):
                if board[i][j] == '.': continue
                elif board[i][j] in a: return False
                elif board[i][j] in nums: a.append(board[i][j])
                else: return False
                
        for i in range(9):
            a = []
            for j in range(9):
                if board[j][i] == '.': continue
                elif board[j][i] in a: return False
                elif board[j][i] in nums: a.append(board[j][i])
                else: return False
        
        for m in range(3):
            for n in range(3):
                a = []
                for i in range(3):
                    for j in range(3):
                        tmp = board[m*3+i][n*3+j]
                        if tmp == '.': continue
                        elif tmp in a: return False
                        elif tmp in nums: a.append(tmp)
                        else: return False
        
        return True