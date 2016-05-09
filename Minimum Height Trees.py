'''
 For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3

return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5

return [3, 4] 
'''

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        s = set(range(n));   d = {i:set() for i in s}
        for u, v in edges:
            d[u].add(v);   d[v].add(u)
        while len(s) > 2:
            leaves = set(x for x in s if len(d[x]) == 1)
            s -= leaves
            for x in leaves:  d[list(d[x])[0]].remove(x)
        return list(s)
'''
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        s = set(range(n));   d = {i:set() for i in s}
        for u, v in edges:
            d[u].add(v);   d[v].add(u)
        while len(s) > 2:
            leaves = set(x for x in s if len(d[x]) == 1)
            s -= leaves
            for x in leaves:
                for y in d[x]:
                    d[y].remove(x)
        return list(s)
'''
#              for x in leaves:  d[list(d[x])[0]].remove(x)
#最多2个。
# Here is one insight for this problem: the root of MHT is the middle point of the longest path in the tree; 
#hence there are at most two MHT roots. 