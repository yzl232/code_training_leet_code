class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(9):
            a = []
            for j in range(9):
                if board[i][j] in a:
                    return False
                elif board[i][j] == '.':
                    continue
                elif board[i][j] in nums:
                    a.append(board[i][j])
                else:
                    return False

            a = []
            for j in range(9):
                if board[j][i] in a:
                    return  False
                elif board[j][i] == '.':
                    continue
                elif board[j][i] in nums:
                    a.append(board[j][i])
                else:
                    return False

        for r in range(3):
            for c in range(3):
                a = []
                for i in range(3):
                    for j in range(3):
                        if board[r*3+i][c*3+j] in a:
                            return False
                        elif board[r*3+i][c*3+j] == '.':
                            continue
                        elif board[r*3+i][c*3+j] in nums:
                            a.append(board[r*3+i][c*3+j])
                        else:
                            return False
        return True