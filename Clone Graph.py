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
    def cloneGraph(self, nodeA):
        self.nodePointers = {}
        if nodeA == None:
            return
        return self.dfs(nodeA)
        
    def dfs(self, nodeA):
        if nodeA in self.nodePointers: 
            return
        else:
            tmp = UndirectedGraphNode(nodeA.label)
            self.nodePointers[nodeA] = tmp

            for i in nodeA.neighbors:
                if i in self.nodePointers:
                    tmp.neighbors.append(self.nodePointers[i])
                    continue
                else:
                    temp_i = self.dfs(i)
                    tmp.neighbors.append(temp_i)
            return tmp