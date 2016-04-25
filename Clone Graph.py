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
    # @DFS   #也是memoization
    def cloneGraph(self, node):
        self.d = {None:None}
        return self.dfs(node)

    def dfs(self, x):   # 如果允许UndirectedNode(x, neighbors), 可以进一步减少2行。
        if x not in self.d:
            self.d[x] = UndirectedGraphNode(x.label)
            self.d[x].neighbors = [self.dfs(y) for y in x.neighbors]
        return self.d[x]

'''
BFS稍微复杂一点点

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return
        nodeB = UndirectedGraphNode(node.label)
        d, pre = {node: nodeB}, [node]
        while pre:
            cur = []
            for x in pre:
                for n in x.neighbors:  #每层把它的所有neighbor都加到cur里边去。(如果没在map)
                    if n in d:  d[x].neighbors.append(d[n])
                    else:
                        cur.append(n)
                        d[n] = UndirectedGraphNode(n.label)
                        d[x].neighbors.append(d[n])
            pre = cur
        return nodeB


'''