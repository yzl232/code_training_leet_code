'''
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1)

Example 2:
Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27) 
'''
'''
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1)

Example 2:
Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27) 
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class Solution(object):
    def depthSum(self, arr):
        self.ret = 0
        self.dfs(arr, 1)
        return self.ret
    
    def dfs(self, arr, depth):
        for x in arr:
            if x.isInteger():  self.ret += x.getInteger() * depth
            else:    self.dfs(x.getList(),depth+1)
        
'''
inner function.  要改变inner function外面的变量， 必须使用self.x

inner function.  如果涉及重新assign某个外面的变量， 就会报错。 得使用self.ret

class Solution(object):
    def depthSum(self, arr):
        """
        :type arr: List[NestedInteger]
        :rtype: int
        """
        self.ret =0
        def dfs(nestedList, depth):
            for x in nestedList:
                if isinstance(x, list):  dfs(x,depth+1)
                else:   self.ret += x * depth
        dfs(arr, 1)
        return self.ret
'''