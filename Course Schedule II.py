'''
 There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]

There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]

There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented. 
'''
class Solution(object):
    def findOrder(self, numCourses, arr):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.graph =  {i:[] for i in range(numCourses)}
        self.visited = {}  # visited最开始为空。
        self.ret = []; self.cycle = False
        for x, y  in arr:
            if y not in self.graph[x]: self.graph[x].append(y)
        for k in self.graph:  self.dfs(k)
        return self.ret if not self.cycle else []

    def dfs(self, x):
        if self.cycle: return
        if x in self.visited:   #已经visit过了
            if self.visited[x]==False:  self.cycle = True  #还没visited完又碰见了， 说明有cycle
            return
        self.visited[x] = False  #这就是与普通dfs的唯一不同。 用False标记
        for y in self.graph[x]: self.dfs(y)
        self.visited[x] = True
        self.ret.append(x)

