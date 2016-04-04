'''
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

    Each 0 marks an empty land which you can pass by freely.

    Each 1 marks a building which you cannot pass through.

    Each 2 marks an obstacle which you cannot pass through.

For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.

Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.

'''
#代码很长。  难倒是没有那么难。 健身房文件。 以前做过。
#


#有障碍。 用BFS
#简单版本在这里   matrix_guard_barrier_保安_障碍
# global 的count矩阵。
class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if board == []: return
        m = len(board); n = len(board[0])  #因为最后结果cnt肯定不为0 。  所以还好
        cnt = [[0 if board[i][j]!='1' else None for j in range(n)] for i in range(m)]  # global 的count矩阵。   只对‘0’ 存数字
        for i in range(m):
            for j in range(n):
                if board[i][j]=='G':
                    tmpCntMatrix = self.bfs(board.copy(), i, j)
                    for x in range(m):
                        for y in range(n):
                            if tmpCntMatrix[x][y]!=None and cnt[x][y]!=None:
                                cnt[x][y]+=tmpCntMatrix[x][y]
        # find min in cnt that is big than 0

    def bfs(self, board, x, y):
        m = len(board); n = len(board[0])
        cntMatrix =  [[None for j in range(n)] for i in range(m)]
        cnt = 0; pre=[(x, y)]; board[x][y] = '#'; cnt[x][y]=0
        while pre:
            cur = set([]);  cnt+=1
            for i, j in pre:
                for r, c in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0<=r<=m-1 and 0<=c<=n-1 and board[r][c]=='0':
                        cur.add((r, c));   board[r][c] = '#'
                        if cntMatrix==None: cntMatrix[r][c]=cnt  #只考虑第一次过去
            pre = cur
        return cntMatrix