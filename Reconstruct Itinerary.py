'''
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

    If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
    All airports are represented by three capital letters (IATA code).
    You may assume all tickets form at least one valid itinerary.

Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].

Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order. 
'''

class Solution(object):
    def findItinerary(self, tickets):
        d, ret ={}, []  #sort.  d里面放更大的值.   因为递归, JFK在最外面了.. 要反一下.      
        for a, b in sorted(tickets)[::-1]:  #题中提到要是最小的lexi order
            if a not in d: d[a] = []     #Eulerian Path. 除了起点, 终点.  都是偶数的degree.  Eulerian Circuit, 则全是偶数degree.
            d[a].append(b)    #  当stuck.  那么说明奇数的degree, 发现了一个终点了.
        def helper(x):
            while x in d and d[x]:  helper(d[x].pop())
            ret.append(x)
        helper('JFK')
        return ret[::-1]


'''  不理解的话, 打印下面的, 配合leetcode图, 就明白了
class Solution(object):
    def findItinerary(self, tickets):
        d, ret ={}, []  #sort.    反向. 因为后面用了pop.
        for a, b in sorted(tickets)[::-1]:  #题中提到要是最小的lexi order
            if a not in d: d[a] = []     #Eulerian Path. 除了起点, 终点.  都是偶数的degree.  Eulerian Circuit, 则全是偶数degree.
            d[a].append(b)
        def helper(x):   #  当stuck.  那么说明奇数的degree, 发现了一个终点了.
            while x in d and d[x]:
                print x, d[x], ret
                helper(d[x].pop())
            ret.append(x)
            print ret
        helper('JFK')
        return ret[::-1]
print Solution().findItinerary([["JFK", "A"], ["A", "C"], ["C", "D"], ["D", "B"], ["D", "A"], ["B", "C"], ["C", "JFK"],  ["JFK", "D"]])

欧拉通路（Eulerian path）：


将机场视为顶点，机票看做有向边，可以构成一个有向图。

    通过图（无向图或有向图）中所有边且每边仅通过一次的通路称为欧拉通路，相应的回路称为欧拉回路。具有欧拉回路的图称为欧拉图（Euler Graph），具有欧拉通路而无欧拉回路的图称为半欧拉图。

'''