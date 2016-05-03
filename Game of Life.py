'''
 According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state.

Follow up:

    Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
    In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

'''

class Solution(object):
    def gameOfLife(self, board):   #很赞. 如果要活着。邻居数目只能是 2<=n<=3.   也就是n=2 or n=3        # (val, cnt) => val
        m, n = len(board), len(board[0]);trans = {(1, 2):1, (0, 3):1, (1, 3):1}
        cur = {(i, j): trans.get((board[i][j], sum( board[x][y] for x in [i-1, i, i+1] for y in [j-1, j, j+1] if (i!=x or j!=y) and (0<=x<m and 0<=y<n))), 0) for i in range(m) for j in range(n) }
        for x,y in cur:  board[x][y] = cur[(x, y)]

'''
class Solution(object):
    def gameOfLife(self, board):
        m, n = len(board), len(board[0]); cur = {}; trans = {(1, 2):1, (0, 3):1, (1, 3):1}
        for i in range(m): #很赞. 如果要活着。邻居数目只能是 2<=n<=3.   也就是n=2 or n=3        # (val, cnt) => val
            for j in range(n):
                cnt = sum( board[x][y] for x in [i-1, i, i+1] for y in [j-1, j, j+1] if (i!=x or j!=y) and (0<=x<m and 0<=y<n))
                cur[(i, j)] =  trans.get((board[i][j], cnt)  , 0)
        for x,y in cur:  board[x][y] = cur[(x, y)]





# 这个是in-place的方法
class Solution(object):
    def gameOfLife(self, board):
        if not board or not board[0]:    return
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):  #下面这行也不是大问题.  最多8个。 每次都是临时的变量而已。
                live = sum( board[x][y]&1 for x in [i-1, i, i+1] for y in [j-1, j, j+1] if (i!=x or j!=y) and (0<=x<m and 0<=y<n))
                if live == 3 or (live == 2 and board[i][j]&1):  board[i][j] +=2
        for i in range(m):
            for j in range(n):
                board[i][j] >>=1
'''





'''
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        trans = { (1, 2): 1, (1, 3): 1, (0, 3): 1 }
        pre = {(i, j):1 for i in range(m) for j in range(n) if board[i][j]==1}  #类似于稀疏矩阵的存储
        cur = {}  #没必要搞pre。
        for r in range(m):
            for c in range(n):
                cnt = sum(pre.get((x,y), 0)for x in[r-1, r, r+1] for y in [c-1, c, c+1] if x!=r or y!=c)  #不算自己
                val = pre.get((r,c),  0)
                if (val, cnt) not in trans: cur[(r,c)]=1
        for r,c in cur: board[r][c] = cur.get((r,c),  0)



# 这个是in-place的方法
class Solution(object):
    def update(self, board, m, n, i, j):
        live = 0
        for p in range(max(i - 1, 0), min(i + 2, m)):
            for q in range(max(j - 1, 0), min(j + 2, n)):
                if p!=i or q!=j: live += board[p][q] & 1
        if live == 3 or (live==2 and (board[i][j] & 1)):  board[i][j] += 2


    def gameOfLife(self, board):
        if not board or not board[0]:
            return
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                self.update(board, m, n, i, j)
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1


To solve it in place, we use 2 bits to store 2 states:

[2nd bit, 1st bit] = [next state, current state]

- 00  dead (next) <- dead (current)
- 01  dead (next) <- live (current)
- 10  live (next) <- dead (current)
- 11  live (next) <- live (current)

    In the beginning, every cell is either 00 or 01.
    Notice that 1st state is independent of 2nd state.
    Imagine all cells are instantly changing from the 1st to the 2nd state, at the same time.
    Let's count # of neighbors from 1st state and set 2nd state bit.
    Since every 2nd state is by default dead, no need to consider transition 01 -> 00.
    In the end, delete every cell's 1st state by doing >> 1.

For each cell's 1st bit, check the 8 pixels around itself, and set the cell's 2nd bit.

    Transition 01 -> 11: when board == 1 and lives >= 2 && lives <= 3.
    Transition 00 -> 10: when board == 0 and lives == 3.

To get the current state, simply do

board[i][j] & 1

To get the next state, simply do

board[i][j] >> 1

'''