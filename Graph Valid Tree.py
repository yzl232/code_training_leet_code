'''


    Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

    For example:

    Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

    Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

    Hint:

    Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], what should your return? Is this case a valid tree? Show More Hint Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
    
    判断输入的边是否能构成一个树，我们需要确定两件事：

        这些边是否构成环路，如果有环则不能构成树

        这些边是否能将所有节点连通，如果有不能连通的节点则不能构成树

    因为不需要知道具体的树长什么样子，只要知道连通的关系，所以并查集相比深度优先搜索是更好的方法。我们定义一个并查集的数据结构，并提供标准的四个接口：

        union 将两个节点放入一个集合中

        find 找到该节点所属的集合编号

        areConnected 判断两个节点是否是一个集合

        count 返回该并查集中有多少个独立的集合

    具体并查集的原理，参见这篇文章。简单来讲，就是先构建一个数组，节点0到节点n-1，刚开始都各自独立的属于自己的集合。这时集合的编号是节点号。然后，每次union操作时，我们把整个并查集中，所有和第一个节点所属集合号相同的节点的集合号，都改成第二个节点的集合号。这样就将一个集合的节点归属到同一个集合号下了。我们遍历一遍输入，把所有边加入我们的并查集中，加的同时判断是否有环路。最后如果并查集中只有一个集合，则说明可以构建树。

'''
class Solution:
    def validTree(self, n, edges):
        self.parent = range(n)
        return len(edges) == n-1 and all(map(self.union, edges))
    def find(self, x):
        return x if self.parent[x] == x else self.find(self.parent[x])
    def union(self, xy):  #union确定没有环, 再加上n-1的长度确定没
        x, y = map(self.find, xy)
        self.parent[x] = y
        return x != y
