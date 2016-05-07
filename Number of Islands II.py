# encoding=utf-8
'''
 Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]

'''
class Solution:
    def numIslands2(self, m, n, positions):
        parent = {}; ret = [] #各个元素都是二院tuple
        def find(x):
            if x!=parent[x]:  parent[x] = find(parent[x])#路径压缩。好！
            return parent[x]#返回parent[x]。 也就是parent根值
        def union(x, y):
            x, y = find(x), find(y)  #如果已经union过了, 之前就是一起的. 返回0
            parent[x] = y
            return x!=y
        for i, j in positions:
            x = (i, j); parent[x] =x
            ret.append((ret[-1] if ret else 0)+1-sum(union(x, y) for y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)] if y in parent))
        return ret
# i, j没管边界问题是因为 y in parent已经考虑了边界了。
'''
可以优化. 加上path compression和size, 来平衡树
class Solution:
    def numIslands2(self, m, n, positions):
        parent, size = {}, {}
        def find(x):
            while parent[x] != x:  x = parent[x]
            return x
        def union(x, y):
            x, y = find(x), find(y)
            if x == y:  return 0
            if size[x] < size[y]:   x, y = y, x
            parent[y] = x
            size[x] += (size[x] == size[y])
            return 1
        counts, count = [], 0
        for i, j in positions:
            x = parent[x] = i, j
            size[x] = 0
            count += 1
            for y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if y in parent:     count -= union(x, y)
            counts.append(count)
        return counts

'''