'''
 Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

     0          3
     |          |
     1 --- 2    4

Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:

     0           4
     |           |
     1 --- 2 --- 3

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1. 
'''
#union-find一般是undirected graph用到的。
class Solution(object):
    def countComponents(self, n, edges):
        p = range(n)
        def find(v):
            if v!=p[v]:  p[v] = find(p[v])#路径压缩。好！
            return p[v]#返回p[v]。 也就是parent根值
        for v, w in edges:
            p[find(v)] = find(w)
        return len(set(find(x) for x in p))