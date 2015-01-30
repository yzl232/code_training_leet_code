'''
 Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

OJ's undirected graph serialization:

Nodes are labeled uniquely.
We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.

As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

    First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
    Second node is labeled as 1. Connect node 1 to node 2.
    Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.

Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/

'''
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    # @DFS
    def cloneGraph(self, node):
        self.d = {}
        if not node: return
        return self.dfs(node)

    def dfs(self, x):
        if x in self.d:  return self.d[x]
        y = UndirectedGraphNode(x.label)
        self.d[x] = y
        for n in x.neighbors:  y.neighbors.append(self.dfs(n))
        return y

'''
BFS稍微复杂一点点


# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, x):
        if not x: return
        y = UndirectedGraphNode(x.label)
        d, pre = {x: y}, [x]   #d兼具已经visited的作用和map node作用
        while pre:
            cur = []
            for x in pre:
                for n in x.neighbors:  #每层把它的所有neighbor都加到cur里边去。(如果没在map)
                    if n not in d:
                        cur.append(n)
                        t = UndirectedGraphNode(n.label)
                        d[n] = t
                    d[x].neighbors.append(d[n])
            pre = cur
        return y


'''