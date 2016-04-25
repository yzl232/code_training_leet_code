
'''
 Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X


'''

class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if board == []: return
        m = len(board); n = len(board[0])
        pre = set([ij for k in range(m+n) for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))])
        while pre:
            cur = set()
            for i, j in pre:
                if not (0<=i<m and 0<=j<n and board[i][j]=='O'): continue
                board[i][j] = '#'
                for r, c in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]: cur.add((r, c))
            pre = cur   # cur.update([(i-1, j), (i+1, j), (i, j-1), (i, j+1)])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O': board[i][j] = 'X'
                elif board[i][j] == '#': board[i][j] = 'O'
'''
class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if board == []: return
        self.m = m = len(board); self.n=n=len(board[0])
        for k in range(max(m, n)):
            for i,j in [(0, k), (m-1, k), (k, 0), (k, m-1)]:
                self.dfs(board, i, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O': board[i][j] = 'X'
                if board[i][j] == '#': board[i][j] = 'O'

    def dfs(self, board, i, j ):
        if not (0<=i<self.m and 0<=j<self.n and board[i][j]=="O"): return
        board[i][j] = '#'
        for r, c in  [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]: self.dfs(board, r, c)


class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if board == []: return
        m = len(board); n = len(board[0])
        pre = set()
        for i in range(m):
            if board[i][0] == 'O': pre.add((i, 0))
            if board[i][n-1] == 'O': pre.add((i, n-1))
        for j in range(n):
            if board[0][j] == 'O': pre.add((0, j))
            if board[m-1][j] == 'O': pre.add((m-1, j))
        while pre:
            cur = set()
            for i, j in pre:
                board[i][j] = '#'
                for r, c in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0<=r<=m-1 and 0<=c<=n-1 and board[r][c]=='O': cur.add((r, c))
            pre = cur
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O': board[i][j] = 'X'
                elif board[i][j] == '#': board[i][j] = 'O'

class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if board == []: return
        m, n = len(board), len(board[0])
        self.m, self.n = m, n
        for i in range(m):
            if board[i][0] == 'O': self.dfs(board, i, 0 )
            if board[i][n-1] == 'O':self.dfs(board, i, n-1)
        for i in range(n):
            if board[0][i] == 'O': self.dfs(board, 0, i)
            if board[m-1][i] == 'O': self.dfs(board ,m-1, i)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O': board[i][j] = 'X'
                if board[i][j] == '#': board[i][j] = 'O'

    def dfs(self, board, i, j ):
        board[i][j] = '#'
        for d in  [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            r = d[0]; c=d[1]
            if 0<=r<=self.m-1 and 0<=c<=self.n-1:
                if board[r][c]=='O': self.dfs(board, r, c)
'''
