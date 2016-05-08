'''
 There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses? 
'''
# encoding=utf-8

class Solution(object):
    def canFinish(self, numCourses, arr):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.graph =  {i:set() for i in range(numCourses)}
        self.ret = True; self.visited = {}  # visited最开始为空。 
        for x, y  in arr:
            if y not in self.graph[x]: self.graph[x].add(y)
        for k in self.graph:  self.dfs(k)
        return self.ret

    def dfs(self, x):
        if not self.ret: return
        if x in self.visited:   #已经visit过了
            if self.visited[x]==False:  self.ret = False
            return
        self.visited[x] = False  #这就是与普通dfs的唯一不同。 用False标记
        for y in self.graph[x]: self.dfs(y)
        self.visited[x] = True


#有向用topological。  无向图用union find

'''

#http://blog.jupo.org/2012/04/06/topological-sorting-acyclic-directed-graphs/
#而且代码其实比较短。 可以背下。
#实际上是O(n2).  用DFS可以做到 O(V)+O(E)
def topolgical_sort(graph_unsorted):
    graph_sorted = []
    graph_unsorted = dict(graph_unsorted)
    while graph_unsorted:
        hasCycle = True
        for node, neighbours in graph_unsorted.items(): #这里用了items()。 后面可以自由修改graph。。相当于array[:]
            for n in neighbours:
                if  n in graph_unsorted:
                    break  #有一个依赖。不用管了。下一个。
            else:  #所有的都不在unsorted。说明没有依赖了。 可以使用。
                hasCycle = False
                del graph_unsorted[node]
                graph_sorted.append((node, neighbours))
        if hasCycle:        #每次都要检查有没有环。
            raise RuntimeError("A cyclic dependency occurred")
    return graph_sorted

#依赖最少的排在前面
graph_unsorted = [(2, []),
                  (5, [11]),
                  (11, [2, 9, 10]),
                  (7, [11, 8]),
                  (9, []),
                  (10, []),
                  (8, [9]),
                  (3, [10, 8])]
print topolgical_sort(graph_unsorted)



'''