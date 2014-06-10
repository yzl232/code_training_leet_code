class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if board == []:  return
        r = len(board); c= len(board[0])
        candidates = set([])
        for i in range(r):
            if board[i][0] == 'O':
                candidates.add((i, 0))

            if board[i][c-1] == 'O': candidates.add((i, c-1))
        for j in range(c):
            if board[0][j] == 'O': candidates.add((0, j))
            if board[r-1][j] == 'O': candidates.add((r-1, j))

        while True:
            if len(candidates)==0: break
            current = set([])
            for t in candidates:
                i = t[0]; j = t[1]
                board[i][j] = '$'
            for t in candidates:
                i = t[0]; j = t[1]
                if i+1<=r-1 and board[i+1][j] == 'O': current.add((i+1, j))
                if i-1>=0 and board[i-1][j] == 'O': current.add((i-1, j))
                if j+1<=c-1 and board[i][j+1] == 'O': current.add((i, j+1))
                if j-1>=0 and board[i][j-1] == 'O': current.add((i, j-1))
            candidates = current
        
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O': board[i][j] = 'X'
                
        for i in range(r):
            for j in range(c):
                if board[i][j] == '$': board[i][j] = 'O'